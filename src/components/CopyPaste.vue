<template>
    <div>

      <b-form-textarea
        id="textarea-small"
        size="md"
        placeholder="Max 500 rows and 25.000 characters (please don't include table headers)"
        :formatter="formatText"
      ></b-form-textarea>
      <p>
          {{copyPasteData}}
      </p>

    </div>
</template>

<script>
//const axios = require('axios')

export default {
    methods:{
        // perform input check
        formatText(e){
            const inpLength = (e).substring(0,25001).length;
            const nRows = e.split(/\r\n|\r|\n/).length;
            
            // !!! add also minimum limit here
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
            copyPasteData: ""
        }
    }
}

</script>

<style>

</style>