<template>
    <div class="">
        Number of rows: {{nRows}}
        <b-form-textarea
            id="textarea-small"
            size="md"
            placeholder="Max 500 rows and 25.000 characters (please don't include table headers)"
            :formatter="formatText"
        ></b-form-textarea>
        <div>
            <label for="steps">Number of Steps</label>
            <b-form-spinbutton id="steps" v-model="nSteps" min="5" :max="nMax"></b-form-spinbutton>
        </div>

        <b-button :disabled="nRows < 50" size="md" @click="postCopyPaste">Make Forecast</b-button>

    </div>
</template>

<script>
const axios = require('axios')

export default {
    methods:{
        
        // axios
        async postCopyPaste() {
            const response = axios.post(
                'http://localhost:5000/copypaste',
                {
                    postData: this.copyPasteData,
                }
            )
            const res = await response;
            console.log(res);
            this.modelRes = res.data;
            return res
        },
        
        // perform input check
        formatText(e){
            const inpLength = (e).substring(0,25001).length;
            const nRows = e.split(/\r\n|\r|\n/).length;
            
            // !!! add also minimum limit, do not accept empty rows etc
            // prevent empty requests
            if ((inpLength < 25000) && (nRows < 500)){
                //set input data
                this.copyPasteData = e;
                //set number of rows from input
                this.nRows = nRows;
                //set max steps allowed
                this.nMax = parseInt(Math.min(30, nRows * .15));
                // lags
                this.nLags = Math.min(20, this.nMax);

                return e;      
            }
            else{
                // input data
                this.copyPasteData = "";
                // number of rows from input
                this.nRows = 0;
                // max steps allowed
                this.nSteps = 5;
                
                return 'Limit exceeded, try with less data.'
            }
        }

    },
    data(){
        return{
            // copy paste data
            copyPasteData: "",
            
            nMax: 0,
            // number of input rows
            nRows: 0,
            // max steps on basis of input data
            nSteps: 5,

            
            // historical and predicted data
            modelRes: "",

        }
    }
}

</script>

<style>

</style>