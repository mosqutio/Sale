// Define tasks
//var tasks = [
//    {name:"理论进度",intervals:[{from:Date.UTC(2014,12,30),to:Date.UTC(2015,01,31)}]},
//    {name:"冯晓彤",intervals:[{from: Date.UTC(2015,01,09),to: Date.UTC(2015,01,10)},{from: Date.UTC(2015,01,12),to: Date.UTC(2015,01,16)},{from: Date.UTC(2015,01,19),to: Date.UTC(2015,01,22)}]},
//    {name:"李　彤",intervals:[{from: Date.UTC(2015,01,13),to: Date.UTC(2015,01,15)},{from: Date.UTC(2015,01,19),to: Date.UTC(2015,01,20)},{from: Date.UTC(2015,01,22),to: Date.UTC(2015,01,22)}]},
//    {name:"李建汉",intervals:[{from: Date.UTC(2015,01,16),to: Date.UTC(2015,01,16)},{from: Date.UTC(2015,01,20),to: Date.UTC(2015,01,20)},{from: Date.UTC(2015,02,09),to: Date.UTC(2015,02,13)}]},
//    {name:"陈明亮",intervals:[{from: Date.UTC(2015,01,15),to: Date.UTC(2015,01,16)},{from: Date.UTC(2015,01,20),to: Date.UTC(2015,01,20)},{from: Date.UTC(2015,01,31),to: Date.UTC(2015,01,31)},{from: Date.UTC(2015,02,03),to: Date.UTC(2015,02,03)},{from: Date.UTC(2015,02,09),to: Date.UTC(2015,02,13)}]}];
var tasks = []
// re-structure the tasks into line seriesvar series = [];
var series = [];


function get_data(){
    $.get("/exhibitions",function(data,status){
        $.each(data.reverse(), function(i, task) {
            var item = {
                name: task.locale,
                data: []
            };
            $.each(task.intervals, function(j, interval) {
                item.data.push({
                    x: interval.from,
                    y: i,
                    label: interval.label,
                    from: interval.from,
                    to: interval.to
                }, {
                    x: interval.to,
                    y: i,
                    from: interval.from,
                    to: interval.to
                });
                // add a null value between intervals
                if (task.intervals[j + 1]) {
                    item.data.push(
                        [(interval.to + task.intervals[j + 1].from) / 2, null]
                    );
                }
            });
            series.push(item);
        });
//        alert("Data: " + data + "\nStatus: " + status);
    });
}

// create the chart
function show_pic(){
var d = get_data()
var chart = new Highcharts.Chart({
    chart: {
        renderTo: 'container'
    },
    title: {
        text: 'Daily activities'
    },
    xAxis: {
        type: 'datetime'
    },
    yAxis: {
        tickInterval: 1,
        labels: {
            formatter: function() {
                if (tasks[this.value]) {
                    return tasks[this.value].name;
                }
            }
        },
        startOnTick: false,
        endOnTick: false,
        title: {
            text: 'Activity'
        },
        minPadding: 0.2,
        maxPadding: 0.2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        formatter: function() {
            return '<b>'+ tasks[this.y].name + '</b><br/>' +
                Highcharts.dateFormat('%Y/%m/%d', this.point.options.from)  +
                ' - ' + Highcharts.dateFormat('%Y/%m/%d', this.point.options.to);
        }
    },
    plotOptions: {
        line: {
            lineWidth: 9,
            //linecap:"square",
            marker: {
                enabled: false
            },
            dataLabels: {
                enabled: true,
                align: 'left',
                formatter: function() {
                    console.log(this.point.options);
                    return this.point.options && this.point.options.label;
                }
            }
        }
    },
    series: series
});
}