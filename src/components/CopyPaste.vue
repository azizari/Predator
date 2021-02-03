<template>
    <div>

      <b-form-textarea
        id="textarea-small"
        size="md"
        placeholder="Max 500 rows and 25.000 characters (please don't include table headers)"
        :formatter="formatText"
      ></b-form-textarea>
      <p>
      </p>
        <h5 @click="postCopyPaste">buttin</h5>
        {{respo}}
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
                {postData: this.copyPasteData}
            )
            const resp = await response
            console.log(resp)
            this.respo = resp.data
            return resp
        },
        
        // perform input check
        formatText(e){
            const inpLength = (e).substring(0,25001).length;
            const nRows = e.split(/\r\n|\r|\n/).length;
            
            // !!! add also minimum limit here
            // prevent empty requests
            if ((inpLength < 25000) && (nRows < 500)){
                this.copyPasteData = e
                return e;      
            }
            else{
                this.copyPasteData = ""
                return 'Limit exceeded, try with less data.'
            }
        }

    },
    data(){
        return{
            copyPasteData: "",
            respo: ""
        }
    }
}

</script>

<style>

</style>