#!/usr/bin/env python
import os
import sys
import yaml
import pdfkit

def prettify(l):
    l = [ip.strip() for ip in l]
    ret = [ "node{}: {}".format(i+1, s) for (i, s) in zip(range(len(l)), l) ]
    return ret


with open(sys.argv[1]) as f:
    data = f.read()

SETTINGS = yaml.load(data)
SETTINGS['footer'] = SETTINGS['footer'].format(url=SETTINGS['url'])
globals().update(SETTINGS)

###############################################################################

ips = list(open("ips.txt"))

print("Current settings (as defined in settings.yaml):")
print("   Number of IPs: {}".format(len(ips)))
print(" VMs per cluster: {}".format(clustersize))
print("Background image: {}".format(background_image))
print

assert len(ips)%clustersize == 0

clusters = []

while ips:
    cluster = ips[:clustersize]
    ips = ips[clustersize:]
    clusters.append(cluster)

html = open("ips.html", "w")
html.write("<html><head><style>")
body = """
div {{ 
    float:left;
    border: 1px solid black;
    width: 28%;
    padding: 4% 2.5% 2.5% 2.5%;
    font-size: x-small;
    background-image: url("{background_image}");
    background-size: 10%;
    background-position-x: 50%;
    background-repeat: no-repeat;
}}
p {{
    margin: 0.5em 0 0.5em 0;
}}
.pagebreak {{
    page-break-before: always;
    clear: both;
    display: block;
    height: 8px;
}}
"""
body = body.format(
     background_image=SETTINGS['background_image'],
)

print(body)
html.write(body)

html.write("</style></head><body>")
for i, cluster in enumerate(clusters):
    if i>0 and i%pagesize==0:
        html.write('<span class="pagebreak"></span>\n')
    html.write("<div>")
    html.write(blurb)
    for s in prettify(cluster):
        html.write("<li>%s</li>\n"%s)
    html.write("</ul></p>")
    html.write("<p>login=docker password=training</p>\n")
    html.write(footer)
    html.write("</div>")
html.close()

with open('ips.html') as f:
    pdfkit.from_file(f, 'ips.pdf')
