#!/usr/bin/env python

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

from rest import *

pwg = 'EXO'
username = 'jruizalv'

database_location = 'MC_Requests.db'
html_location = ''

mcm = McM(dev=False)

RequestsToClone=[
'EXO-RunIISummer15wmLHEGS-06757',
'EXO-RunIISummer15wmLHEGS-06758',
'EXO-RunIISummer15wmLHEGS-06759',
'EXO-RunIISummer15wmLHEGS-06760',
'EXO-RunIISummer15wmLHEGS-06761',
'EXO-RunIISummer15wmLHEGS-06762',
'EXO-RunIISummer15wmLHEGS-06763',
'EXO-RunIISummer15wmLHEGS-06764',
'EXO-RunIISummer15wmLHEGS-06765',
'EXO-RunIISummer15wmLHEGS-06766',
'EXO-RunIISummer15wmLHEGS-06767',
'EXO-RunIISummer15wmLHEGS-06768',
'EXO-RunIISummer15wmLHEGS-06769',
'EXO-RunIISummer15wmLHEGS-06770',
'EXO-RunIISummer15wmLHEGS-06771',
'EXO-RunIISummer15wmLHEGS-06772',
'EXO-RunIISummer15wmLHEGS-06773',
'EXO-RunIISummer15wmLHEGS-06774',
'EXO-RunIISummer15wmLHEGS-06775',
'EXO-RunIISummer15wmLHEGS-06776',
'EXO-RunIISummer15wmLHEGS-06777',
'EXO-RunIISummer15wmLHEGS-06778',
'EXO-RunIISummer15wmLHEGS-06779',
'EXO-RunIISummer15wmLHEGS-06780',
'EXO-RunIISummer15wmLHEGS-06781',
'EXO-RunIISummer15wmLHEGS-06782',
'EXO-RunIISummer15wmLHEGS-06783',
'EXO-RunIISummer15wmLHEGS-06784',
'EXO-RunIISummer15wmLHEGS-06785',
'EXO-RunIISummer15wmLHEGS-06786',
'EXO-RunIISummer15wmLHEGS-06787',
'EXO-RunIISummer15wmLHEGS-06788',
'EXO-RunIISummer15wmLHEGS-06789',
'EXO-RunIISummer15wmLHEGS-06790',
'EXO-RunIISummer15wmLHEGS-06791',
'EXO-RunIISummer15wmLHEGS-06792',
'EXO-RunIISummer15wmLHEGS-06793',
'EXO-RunIISummer15wmLHEGS-06794',
'EXO-RunIISummer15wmLHEGS-06795',
'EXO-RunIISummer15wmLHEGS-06796',
'EXO-RunIISummer15wmLHEGS-06797',
'EXO-RunIISummer15wmLHEGS-06798',
'EXO-RunIISummer15wmLHEGS-06799',
'EXO-RunIISummer15wmLHEGS-06800',
'EXO-RunIISummer15wmLHEGS-06801',
'EXO-RunIISummer15wmLHEGS-06802',
'EXO-RunIISummer15wmLHEGS-06803',
'EXO-RunIISummer15wmLHEGS-06804',
'EXO-RunIISummer15wmLHEGS-06805',
'EXO-RunIISummer15wmLHEGS-06806',
'EXO-RunIISummer15wmLHEGS-06807',
'EXO-RunIISummer15wmLHEGS-06808',
'EXO-RunIISummer15wmLHEGS-06809',
'EXO-RunIISummer15wmLHEGS-06810',
'EXO-RunIISummer15wmLHEGS-06811',
'EXO-RunIISummer15wmLHEGS-06812',
'EXO-RunIISummer15wmLHEGS-06813',
'EXO-RunIISummer15wmLHEGS-06814',
'EXO-RunIISummer15wmLHEGS-06815',
'EXO-RunIISummer15wmLHEGS-06816',
'EXO-RunIISummer15wmLHEGS-06817',
'EXO-RunIISummer15wmLHEGS-06818',
'EXO-RunIISummer15wmLHEGS-06819',
'EXO-RunIISummer15wmLHEGS-06820',
'EXO-RunIISummer15wmLHEGS-06821',
'EXO-RunIISummer15wmLHEGS-06822',
'EXO-RunIISummer15wmLHEGS-06823',
'EXO-RunIISummer15wmLHEGS-06824',
'EXO-RunIISummer15wmLHEGS-06825',
'EXO-RunIISummer15wmLHEGS-06826',
'EXO-RunIISummer15wmLHEGS-06827',
'EXO-RunIISummer15wmLHEGS-06828',
'EXO-RunIISummer15wmLHEGS-06829',
'EXO-RunIISummer15wmLHEGS-06830',
'EXO-RunIISummer15wmLHEGS-06831',
'EXO-RunIISummer15wmLHEGS-06832',
'EXO-RunIISummer15wmLHEGS-06833',
'EXO-RunIISummer15wmLHEGS-06834',
'EXO-RunIISummer15wmLHEGS-06835',
'EXO-RunIISummer15wmLHEGS-06836',
'EXO-RunIISummer15wmLHEGS-06837',
'EXO-RunIISummer15wmLHEGS-06838',
'EXO-RunIISummer15wmLHEGS-06839',
'EXO-RunIISummer15wmLHEGS-06840',
'EXO-RunIISummer15wmLHEGS-06841',
'EXO-RunIISummer15wmLHEGS-06842',
'EXO-RunIISummer15wmLHEGS-06843',
'EXO-RunIISummer15wmLHEGS-06844',
'EXO-RunIISummer15wmLHEGS-06845',
'EXO-RunIISummer15wmLHEGS-06846',
'EXO-RunIISummer15wmLHEGS-06847',
'EXO-RunIISummer15wmLHEGS-06848',
'EXO-RunIISummer15wmLHEGS-06849',
'EXO-RunIISummer15wmLHEGS-06850',
'EXO-RunIISummer15wmLHEGS-06851',
'EXO-RunIISummer15wmLHEGS-06852',
'EXO-RunIISummer15wmLHEGS-06853',
'EXO-RunIISummer15wmLHEGS-06854',
'EXO-RunIISummer15wmLHEGS-06855',
'EXO-RunIISummer15wmLHEGS-06856',
'EXO-RunIISummer15wmLHEGS-06857',
'EXO-RunIISummer15wmLHEGS-06858',
'EXO-RunIISummer15wmLHEGS-06859',
'EXO-RunIISummer15wmLHEGS-06860',
'EXO-RunIISummer15wmLHEGS-06861',
'EXO-RunIISummer15wmLHEGS-06862',
'EXO-RunIISummer15wmLHEGS-06863',
'EXO-RunIISummer15wmLHEGS-06864',
'EXO-RunIISummer15wmLHEGS-06865',
'EXO-RunIISummer15wmLHEGS-06866',
'EXO-RunIISummer15wmLHEGS-06867',
'EXO-RunIISummer15wmLHEGS-06868',
'EXO-RunIISummer15wmLHEGS-06869',
'EXO-RunIISummer15wmLHEGS-06870',
'EXO-RunIISummer15wmLHEGS-06871',
'EXO-RunIISummer15wmLHEGS-06872',
'EXO-RunIISummer15wmLHEGS-06873',
'EXO-RunIISummer15wmLHEGS-06874',
'EXO-RunIISummer15wmLHEGS-06875',
'EXO-RunIISummer15wmLHEGS-06876',
'EXO-RunIISummer15wmLHEGS-06877',
'EXO-RunIISummer15wmLHEGS-06878',
'EXO-RunIISummer15wmLHEGS-06879',
'EXO-RunIISummer15wmLHEGS-06880',
'EXO-RunIISummer15wmLHEGS-06881',
'EXO-RunIISummer15wmLHEGS-06882',
'EXO-RunIISummer15wmLHEGS-06883',
'EXO-RunIISummer15wmLHEGS-06884',
'EXO-RunIISummer15wmLHEGS-06885',
'EXO-RunIISummer15wmLHEGS-06886',
'EXO-RunIISummer15wmLHEGS-06887',
'EXO-RunIISummer15wmLHEGS-06888',
'EXO-RunIISummer15wmLHEGS-06889',
'EXO-RunIISummer15wmLHEGS-06890',
'EXO-RunIISummer15wmLHEGS-06891',
'EXO-RunIISummer15wmLHEGS-06892',
'EXO-RunIISummer15wmLHEGS-06893',
'EXO-RunIISummer15wmLHEGS-06894',
'EXO-RunIISummer15wmLHEGS-06895',
'EXO-RunIISummer15wmLHEGS-06896',
'EXO-RunIISummer15wmLHEGS-06897',
'EXO-RunIISummer15wmLHEGS-06898',
'EXO-RunIISummer15wmLHEGS-06899',
'EXO-RunIISummer15wmLHEGS-06900',
'EXO-RunIISummer15wmLHEGS-06901',
'EXO-RunIISummer15wmLHEGS-06902',
'EXO-RunIISummer15wmLHEGS-06903',
'EXO-RunIISummer15wmLHEGS-06904',
'EXO-RunIISummer15wmLHEGS-06905',
'EXO-RunIISummer15wmLHEGS-06906',
'EXO-RunIISummer15wmLHEGS-06907',
'EXO-RunIISummer15wmLHEGS-06908',
'EXO-RunIISummer15wmLHEGS-06909',
'EXO-RunIISummer15wmLHEGS-06910',
'EXO-RunIISummer15wmLHEGS-06911',
'EXO-RunIISummer15wmLHEGS-06912',
'EXO-RunIISummer15wmLHEGS-06913',
'EXO-RunIISummer15wmLHEGS-06914',
'EXO-RunIISummer15wmLHEGS-06915',
'EXO-RunIISummer15wmLHEGS-06916',
'EXO-RunIISummer15wmLHEGS-06917',
'EXO-RunIISummer15wmLHEGS-06918',
'EXO-RunIISummer15wmLHEGS-06919',
'EXO-RunIISummer15wmLHEGS-06920',
'EXO-RunIISummer15wmLHEGS-06921',
'EXO-RunIISummer15wmLHEGS-06922',
'EXO-RunIISummer15wmLHEGS-06923',
'EXO-RunIISummer15wmLHEGS-06924',
'EXO-RunIISummer15wmLHEGS-06925',
'EXO-RunIISummer15wmLHEGS-06926',
'EXO-RunIISummer15wmLHEGS-06927',
'EXO-RunIISummer15wmLHEGS-06928',
'EXO-RunIISummer15wmLHEGS-06929',
'EXO-RunIISummer15wmLHEGS-06930',
'EXO-RunIISummer15wmLHEGS-06931',
'EXO-RunIISummer15wmLHEGS-06932',
'EXO-RunIISummer15wmLHEGS-06933',
'EXO-RunIISummer15wmLHEGS-06934',
'EXO-RunIISummer15wmLHEGS-06935',
'EXO-RunIISummer15wmLHEGS-06936',
'EXO-RunIISummer15wmLHEGS-06937',
'EXO-RunIISummer15wmLHEGS-06938',
'EXO-RunIISummer15wmLHEGS-06939',
'EXO-RunIISummer15wmLHEGS-06940',
'EXO-RunIISummer15wmLHEGS-06941',
'EXO-RunIISummer15wmLHEGS-06942',
'EXO-RunIISummer15wmLHEGS-06943',
'EXO-RunIISummer15wmLHEGS-06944',
'EXO-RunIISummer15wmLHEGS-06945',
'EXO-RunIISummer15wmLHEGS-06946',
'EXO-RunIISummer15wmLHEGS-06947',
'EXO-RunIISummer15wmLHEGS-06948',
'EXO-RunIISummer15wmLHEGS-06949',
'EXO-RunIISummer15wmLHEGS-06950',
'EXO-RunIISummer15wmLHEGS-06951',
'EXO-RunIISummer15wmLHEGS-06952',
'EXO-RunIISummer15wmLHEGS-06953',
'EXO-RunIISummer15wmLHEGS-06954',
'EXO-RunIISummer15wmLHEGS-06955',
'EXO-RunIISummer15wmLHEGS-06956',
'EXO-RunIISummer15wmLHEGS-06957',
'EXO-RunIISummer15wmLHEGS-06958',
'EXO-RunIISummer15wmLHEGS-06959',
'EXO-RunIISummer15wmLHEGS-06960',
'EXO-RunIISummer15wmLHEGS-06961',
'EXO-RunIISummer15wmLHEGS-06962',
'EXO-RunIISummer15wmLHEGS-06963',
'EXO-RunIISummer15wmLHEGS-06964',
'EXO-RunIISummer15wmLHEGS-06965',
'EXO-RunIISummer15wmLHEGS-06966',
'EXO-RunIISummer15wmLHEGS-06967',
'EXO-RunIISummer15wmLHEGS-06968',
'EXO-RunIISummer15wmLHEGS-06969',
'EXO-RunIISummer15wmLHEGS-06970',
'EXO-RunIISummer15wmLHEGS-06971',
'EXO-RunIISummer15wmLHEGS-06972',
'EXO-RunIISummer15wmLHEGS-06973',
'EXO-RunIISummer15wmLHEGS-06974',
'EXO-RunIISummer15wmLHEGS-06975',
'EXO-RunIISummer15wmLHEGS-06976',
'EXO-RunIISummer15wmLHEGS-06977',
'EXO-RunIISummer15wmLHEGS-06978',
'EXO-RunIISummer15wmLHEGS-06979',
'EXO-RunIISummer15wmLHEGS-06980',
'EXO-RunIISummer15wmLHEGS-06981'
]

for request_prepid_to_clone in RequestsToClone:
    request = mcm.get('requests', request_prepid_to_clone)
    request[u'dataset_name'] = request[u'dataset_name'].replace("TuneCUEP8M1","TuneCUETP8M1")
    update_answer = mcm.update('requests', request) 
    print(request_prepid_to_clone)
    print(update_answer)
    #if update_answer.get('results'):
    #    print('Modified PrepID: %s' % (clone_answer['prepid']))
    #else:
    #    print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))



