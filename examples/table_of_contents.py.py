import docraptor

doc_api = docraptor.DocApi()
# this key works in test mode!
doc_api.api_client.configuration.username = 'YOUR_API_KEY_HERE'

document_content = r"""
    <div id="toc">
       <h3>Table of Contents</h3>
    </div>
    <div id="contents">
       <h1>Main Heading (h1)</h1>
       <h2>Second level heading (h2)</h2>
       <h2>Another heading (h2)</h2>
       <h3>Sub heading (h3)</h3>
       <h2>One more second level heading (h2)</h2>
    </div>

    <script>
      window.onload = function () {
        var toc = "";
        var level = 0;

        document.getElementById("contents").innerHTML =
        document.getElementById("contents").innerHTML.replace(/<h([\d])>([^<]+)<\/h([\d])>/gi,
          function (str, openLevel, titleText, closeLevel) {
            if (openLevel != closeLevel) {
              return str;
            }

            if (openLevel > level) {
              toc += (new Array(openLevel - level + 1)).join("<ul>");
            } else if (openLevel < level) {
              toc += (new Array(level - openLevel + 1)).join("</ul>");
            }

            level = parseInt(openLevel);

            var anchor = titleText.replace(/ /g, "_");
            toc += "<li><a href=\"#" + anchor + "\">" + titleText + "</a></li>";

            return "<h" + openLevel + "><a name=\"" + anchor + "\">" + titleText + "</a></h" + closeLevel + ">";
          }
        );

        if (level) {
          toc += (new Array(level + 1)).join("</ul>");
        }

        document.getElementById("toc").innerHTML += toc;
      };
    </script>

    <style>
      #toc li a::after {
        content: " | Page " target-counter(attr(href), page);
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
    with open('table-of-contents.pdf', 'w+b') as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()
    print('Successfully created table-of-contents.pdf!')
except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
