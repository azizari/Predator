<template>
    <div class="">

      <b-form-textarea
        id="textarea-small"
        size="md"
        placeholder="Max 500 rows and 25.000 characters (please don't include table headers)"
        :formatter="formatText"
      ></b-form-textarea>
      <p>
      </p>
        <h5 @click="postCopyPaste">buttin</h5>
        {{modelRes}}
        {{nRows}}
        {{nSteps}}
    
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
            
            // !!! add also minimum limit here
            // prevent empty requests
            if ((inpLength < 25000) && (nRows < 500)){
                //set input data
                this.copyPasteData = e;
                //set number of rows from input
                this.nRows = nRows;
                //set max steps allowed
                this.nSteps = Math.min(30, parseInt(nRows * .15));
                
                return e;      
            }
            else{
                // input data
                this.copyPasteData = "";
                // number of rows from input
                this.nRows = "";
                // max steps allowed
                this.nSteps = "";
                
                return 'Limit exceeded, try with less data.'
            }
        }

    },
    data(){
        return{
            // copy paste data
            copyPasteData: "",
            // number of input rows
            nRows: "",
            // max steps on basis of input data
            nSteps: "",
            // historical and predicted data
            modelRes: "",

        }
    }
}

</script>

<style>

</style>