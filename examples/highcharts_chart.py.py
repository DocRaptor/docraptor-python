import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

document_content = r"""
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <div id="container" style="height: 816px; width: 1056px;"></div>

    <script>
      Highcharts.chart('container', {
        chart: {
          plotBackgroundColor: null,
          plotBorderWidth: null,
          plotShadow: false,
          type: 'pie'
        },
        title: {
          text: 'Browser market shares January, 2015 to May, 2015'
        },
        tooltip: {
          pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
          pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
              enabled: false
            },
            showInLegend: true
          }
        },
        series: [{
          name: 'Brands',
          colorByPoint: true,
          data: [{
            name: 'Microsoft Internet Explorer',
            y: 56.33
          }, {
            name: 'Chrome',
            y: 24.03,
            sliced: true,
            selected: true
          }, {
            name: 'Firefox',
            y: 10.38
          }, {
            name: 'Safari',
            y: 4.77
          }, {
            name: 'Opera',
            y: 0.91
          }, {
            name: 'Proprietary or Undetectable',
            y: 0.2
          }]
        }],
        accessibility: {
          enabled: false
        }
      });
      var didWait = false;
      docraptorJavaScriptFinished = function() {
        if (! didWait) {
          setTimeout(function(){
            didWait = true;
          }, 2000);
          return false;
        }
        return true;
      }
    </script>

    <style>
      @page {
        size: landscape;
        margin: 0;
      }
    </style>
"""

try:
    response = doc_api.create_doc({
        'test': True,  # test documents are free but watermarked
        'document_type': 'pdf',
        'document_content': document_content,
        # 'document_url': 'https://docraptor.com/examples/invoice.html',
        'javascript': True,
        # 'prince_options': # {
        #    'media': 'print', # @media 'screen' or 'print' CSS
        #    'baseurl': 'https://yoursite.com', # the base URL for any relative URLs
        # },
    })

    # create_doc() returns a binary string
    with open('highcharts-chart.pdf', 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print('Successfully created highcharts-chart.pdf!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
