import requests
import json
from flask import Flask, jsonify
import urllib3
import ssl
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

#SCRIPT MONKEY-HK4 Ñ 
# API MINSA
app = Flask(__name__)
@app.route('/minsa/api/dni=<string:documinsa>')
def apibono(documinsa):
    url_minsa = "https://websalud.minsa.gob.pe/hisminsa/his/paciente"
    headers = {}
    headers["Accept"] = "application/x-www-form-urlencoded"
    #headers["Cookie"] = 'JSESSIONID=1B10DFA6BF799B8B5A61B99AC84BB985; _ga_FWED2G8KFJ=GS1.1.1638361984.7.1.1638362497.0; _ga=GA1.3.912660399.1635797699; _ga_TF36D8Y64K=GS1.1.1637966571.1.0.1637966578.0; _ga_YT8P5VMSKV=GS1.1.1639163708.1.0.1639163708.0; _ga_5SG0KRSQDH=GS1.1.1639163709.1.1.1639164153.0; rxVisitor=16427835718470F88A4VDPCIM5ANIH8TC8MUID2KSQ8F7; dtPC=2$584243483_126h-vJNAALWEODDUHNJPGMNIHGHINONAKNDMS; rxvt=1642786195026|1642783571874; dtSa=true%7CC%7C-1%7CClose%20Tab%7C-%7C1642784293525%7C584243483_126%7Chttps%3A%2F%2Fwebsalud.minsa.gob.pe%2Fsaludescolar%2Fview%2Fregistros%2Fatenciones%2Fatencionescolar.jsp%7CApp%20Salud%20Escolar%20-%20HIS%20MINSA%7C1642784254494%7C; dtLatC=61; byt=3ab58cabc403ef7c62056ec299e3f049748cb43f5bde60bf7f9d0304bf6becfc5ae21730e1cafb73b97112fd8cb72a91dfb167885031c16509c53401018c63586e1b816636cb573d4c974c7d168aa5931ad81bcf9cbb43743897a65dbc5d02d4; dtCookie=2$8C42DF7C42D18892FB043095881DA1CB|HISMINSA|1|RUM+Default+Application|1'
    headers["Cookie"] = 'JSESSIONID=C6D2D2A0F5F7BEF52C6C759EF8FE74EF; cf_clearance=XmAuLzaFsVyC2jB3LU.YNgjm7u91RuOa3GUof_Ke9Wc-1656886383-0-150; byt=cf2c79605770f002e7346eeca98505e2748cb43f5bde60bf3d541249b350b1ad66d2f109945d7915b793baa54b54c1762c68de06ed08585658b1cfdaafbb7932445897e41c8acb70016fc65b20fbb8144f0290c63c414b83fd9c0b08e233b833z'
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
    headers["Origin"] = "https://websalud.minsa.gob.pe"
    headers["Referer"] = "https://websalud.minsa.gob.pe/hisminsa/"

    resp = requests.post(url_minsa, headers=headers, data={
        'C': 'PACIENTE',
        'S': 'INFOGETBYID',
        'idtipodoc': '1',
        'numdoc': documinsa
    })
    re = json.loads(resp.text)
    return jsonify(re)

if __name__ == "__main__":
    app.run(debug=True, port=4000)
