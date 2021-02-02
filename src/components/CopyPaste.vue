<template>
    <div>


      <b-form-textarea
        id="textarea-small"
        size="md"
        placeholder="Max 500 rows and 25.000 characters (please don't include table headers)"
        :formatter="formatText"
      ></b-form-textarea>

    </div>
</template>

<script>

export default {


methods:{
    // perform input check
    formatText(e){
        const inpLength = (e).substring(0,25001).length;
        const nRows = e.split(/\r\n|\r|\n/).length;
        
        if ((inpLength < 25000) && (nRows < 500 && nRows > 50)){
            console.log("2020-11-12 15".replace('\t', ''))
            return e;      
        }
        else{
            return 'Limit exceeded, try with less data.'
        }
    }

}


}
</script>

<style>

</style>