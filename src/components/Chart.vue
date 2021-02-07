<script>
import {Line} from 'vue-chartjs'

export default {
	extends: Line,
	props: {
		chartData: Array,
		chartOptions:{responsive:true}
	},
	
	computed:{
		// use chartData from props
		computeData: function(){return{
			// select x-axis labels
			labels: this.chartData.map(x => new Date(x[0]).toDateString()),
			datasets: [
				// select y-axis values
				{
					data: this.chartData.map(x => x[1])
				}
			]}
		}		
	},
	watch: {
		// trigger chart rendering if chartData gets updates
		chartData: function() {
			this.renderChart(this.computeData, this.chartOptions);
		}
	},
	mounted () {
		// trigger chart rendering on initial load
		this.renderChart()
	},

    data(){
        return{
            placeHolder: {
			// select x-axis labels
			labels: [0,1,2,3],
			datasets: [
				// select y-axis values
				{
					data: [0,1,2,3]
				}
			]}
        }
    }
}
</script>