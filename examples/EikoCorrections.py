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
'EXO-RunIISummer15wmLHEGS-06049',
'EXO-RunIISummer15wmLHEGS-06050',
'EXO-RunIISummer15wmLHEGS-06051',
'EXO-RunIISummer15wmLHEGS-06052',
'EXO-RunIISummer15wmLHEGS-06053',
'EXO-RunIISummer15wmLHEGS-06054',
'EXO-RunIISummer15wmLHEGS-06055',
'EXO-RunIISummer15wmLHEGS-06056',
'EXO-RunIISummer15wmLHEGS-06057',
'EXO-RunIISummer15wmLHEGS-06058',
'EXO-RunIISummer15wmLHEGS-06059',
'EXO-RunIISummer15wmLHEGS-06060',
'EXO-RunIISummer15wmLHEGS-06061',
'EXO-RunIISummer15wmLHEGS-06062',
'EXO-RunIISummer15wmLHEGS-06063',
'EXO-RunIISummer15wmLHEGS-06064',
'EXO-RunIISummer15wmLHEGS-06065',
'EXO-RunIISummer15wmLHEGS-06066',
'EXO-RunIISummer15wmLHEGS-06067',
'EXO-RunIISummer15wmLHEGS-06068',
'EXO-RunIISummer15wmLHEGS-06069',
'EXO-RunIISummer15wmLHEGS-06070',
'EXO-RunIISummer15wmLHEGS-06071',
'EXO-RunIISummer15wmLHEGS-06072',
'EXO-RunIISummer15wmLHEGS-06073',
'EXO-RunIISummer15wmLHEGS-06074',
'EXO-RunIISummer15wmLHEGS-06075',
'EXO-RunIISummer15wmLHEGS-06076',
'EXO-RunIISummer15wmLHEGS-06077',
'EXO-RunIISummer15wmLHEGS-06078',
'EXO-RunIISummer15wmLHEGS-06079',
'EXO-RunIISummer15wmLHEGS-06080',
'EXO-RunIISummer15wmLHEGS-06081',
'EXO-RunIISummer15wmLHEGS-06082',
'EXO-RunIISummer15wmLHEGS-06083',
'EXO-RunIISummer15wmLHEGS-06084',
'EXO-RunIISummer15wmLHEGS-06085',
'EXO-RunIISummer15wmLHEGS-06086',
'EXO-RunIISummer15wmLHEGS-06087',
'EXO-RunIISummer15wmLHEGS-06088',
'EXO-RunIISummer15wmLHEGS-06089',
'EXO-RunIISummer15wmLHEGS-06090',
'EXO-RunIISummer15wmLHEGS-06091',
'EXO-RunIISummer15wmLHEGS-06092',
'EXO-RunIISummer15wmLHEGS-06093',
'EXO-RunIISummer15wmLHEGS-06094',
'EXO-RunIISummer15wmLHEGS-06095',
'EXO-RunIISummer15wmLHEGS-06096',
'EXO-RunIISummer15wmLHEGS-06097',
'EXO-RunIISummer15wmLHEGS-06098',
'EXO-RunIISummer15wmLHEGS-06099',
'EXO-RunIISummer15wmLHEGS-06100',
'EXO-RunIISummer15wmLHEGS-06101',
'EXO-RunIISummer15wmLHEGS-06102',
'EXO-RunIISummer15wmLHEGS-06103',
'EXO-RunIISummer15wmLHEGS-06104',
'EXO-RunIISummer15wmLHEGS-06105',
'EXO-RunIISummer15wmLHEGS-06106',
'EXO-RunIISummer15wmLHEGS-06107',
'EXO-RunIISummer15wmLHEGS-06108',
'EXO-RunIISummer15wmLHEGS-06109',
'EXO-RunIISummer15wmLHEGS-06110',
'EXO-RunIISummer15wmLHEGS-06111',
'EXO-RunIISummer15wmLHEGS-06112',
'EXO-RunIISummer15wmLHEGS-06113',
'EXO-RunIISummer15wmLHEGS-06114',
'EXO-RunIISummer15wmLHEGS-06115',
'EXO-RunIISummer15wmLHEGS-06116',
'EXO-RunIISummer15wmLHEGS-06117',
'EXO-RunIISummer15wmLHEGS-06118',
'EXO-RunIISummer15wmLHEGS-06119',
'EXO-RunIISummer15wmLHEGS-06120',
'EXO-RunIISummer15wmLHEGS-06121',
'EXO-RunIISummer15wmLHEGS-06122',
'EXO-RunIISummer15wmLHEGS-06123',
'EXO-RunIISummer15wmLHEGS-06124',
'EXO-RunIISummer15wmLHEGS-06125',
'EXO-RunIISummer15wmLHEGS-06126',
'EXO-RunIISummer15wmLHEGS-06127',
'EXO-RunIISummer15wmLHEGS-06128',
'EXO-RunIISummer15wmLHEGS-06129',
'EXO-RunIISummer15wmLHEGS-06130',
'EXO-RunIISummer15wmLHEGS-06131',
'EXO-RunIISummer15wmLHEGS-06132',
'EXO-RunIISummer15wmLHEGS-06133',
'EXO-RunIISummer15wmLHEGS-06134',
'EXO-RunIISummer15wmLHEGS-06135',
'EXO-RunIISummer15wmLHEGS-06136',
'EXO-RunIISummer15wmLHEGS-06137',
'EXO-RunIISummer15wmLHEGS-06138',
'EXO-RunIISummer15wmLHEGS-06139',
'EXO-RunIISummer15wmLHEGS-06140',
'EXO-RunIISummer15wmLHEGS-06141',
'EXO-RunIISummer15wmLHEGS-06142',
'EXO-RunIISummer15wmLHEGS-06143',
'EXO-RunIISummer15wmLHEGS-06144',
'EXO-RunIISummer15wmLHEGS-06145',
'EXO-RunIISummer15wmLHEGS-06146',
'EXO-RunIISummer15wmLHEGS-06147',
'EXO-RunIISummer15wmLHEGS-06148',
'EXO-RunIISummer15wmLHEGS-06149',
'EXO-RunIISummer15wmLHEGS-06150',
'EXO-RunIISummer15wmLHEGS-06151',
'EXO-RunIISummer15wmLHEGS-06152',
'EXO-RunIISummer15wmLHEGS-06153',
'EXO-RunIISummer15wmLHEGS-06154',
'EXO-RunIISummer15wmLHEGS-06155',
'EXO-RunIISummer15wmLHEGS-06156',
'EXO-RunIISummer15wmLHEGS-06157',
'EXO-RunIISummer15wmLHEGS-06158',
'EXO-RunIISummer15wmLHEGS-06159',
'EXO-RunIISummer15wmLHEGS-06160',
'EXO-RunIISummer15wmLHEGS-06161',
'EXO-RunIISummer15wmLHEGS-06162',
'EXO-RunIISummer15wmLHEGS-06163',
'EXO-RunIISummer15wmLHEGS-06164',
'EXO-RunIISummer15wmLHEGS-06165',
'EXO-RunIISummer15wmLHEGS-06166',
'EXO-RunIISummer15wmLHEGS-06167',
'EXO-RunIISummer15wmLHEGS-06168',
'EXO-RunIISummer15wmLHEGS-06169',
'EXO-RunIISummer15wmLHEGS-06170',
'EXO-RunIISummer15wmLHEGS-06171',
'EXO-RunIISummer15wmLHEGS-06172',
'EXO-RunIISummer15wmLHEGS-06173',
'EXO-RunIISummer15wmLHEGS-06174',
'EXO-RunIISummer15wmLHEGS-06175',
'EXO-RunIISummer15wmLHEGS-06176',
'EXO-RunIISummer15wmLHEGS-06177',
'EXO-RunIISummer15wmLHEGS-06178',
'EXO-RunIISummer15wmLHEGS-06179',
'EXO-RunIISummer15wmLHEGS-06180',
'EXO-RunIISummer15wmLHEGS-06181',
'EXO-RunIISummer15wmLHEGS-06182',
'EXO-RunIISummer15wmLHEGS-06183',
'EXO-RunIISummer15wmLHEGS-06184',
'EXO-RunIISummer15wmLHEGS-06185',
'EXO-RunIISummer15wmLHEGS-06186',
'EXO-RunIISummer15wmLHEGS-06187',
'EXO-RunIISummer15wmLHEGS-06188',
'EXO-RunIISummer15wmLHEGS-06189',
'EXO-RunIISummer15wmLHEGS-06190',
'EXO-RunIISummer15wmLHEGS-06191',
'EXO-RunIISummer15wmLHEGS-06192',
'EXO-RunIISummer15wmLHEGS-06193',
'EXO-RunIISummer15wmLHEGS-06194',
'EXO-RunIISummer15wmLHEGS-06195',
'EXO-RunIISummer15wmLHEGS-06196',
'EXO-RunIISummer15wmLHEGS-06197',
'EXO-RunIISummer15wmLHEGS-06198',
'EXO-RunIISummer15wmLHEGS-06199',
'EXO-RunIISummer15wmLHEGS-06200',
'EXO-RunIISummer15wmLHEGS-06201',
'EXO-RunIISummer15wmLHEGS-06202',
'EXO-RunIISummer15wmLHEGS-06203',
'EXO-RunIISummer15wmLHEGS-06204',
'EXO-RunIISummer15wmLHEGS-06205',
'EXO-RunIISummer15wmLHEGS-06206',
'EXO-RunIISummer15wmLHEGS-06207',
'EXO-RunIISummer15wmLHEGS-06208',
'EXO-RunIISummer15wmLHEGS-06209',
'EXO-RunIISummer15wmLHEGS-06210',
'EXO-RunIISummer15wmLHEGS-06211',
'EXO-RunIISummer15wmLHEGS-06212',
'EXO-RunIISummer15wmLHEGS-06213',
'EXO-RunIISummer15wmLHEGS-06214',
'EXO-RunIISummer15wmLHEGS-06215',
'EXO-RunIISummer15wmLHEGS-06216',
'EXO-RunIISummer15wmLHEGS-06217',
'EXO-RunIISummer15wmLHEGS-06218',
'EXO-RunIISummer15wmLHEGS-06219',
'EXO-RunIISummer15wmLHEGS-06220',
'EXO-RunIISummer15wmLHEGS-06221',
'EXO-RunIISummer15wmLHEGS-06222',
'EXO-RunIISummer15wmLHEGS-06223',
'EXO-RunIISummer15wmLHEGS-06224',
'EXO-RunIISummer15wmLHEGS-06225',
'EXO-RunIISummer15wmLHEGS-06226',
'EXO-RunIISummer15wmLHEGS-06227',
'EXO-RunIISummer15wmLHEGS-06228',
'EXO-RunIISummer15wmLHEGS-06229',
'EXO-RunIISummer15wmLHEGS-06230',
'EXO-RunIISummer15wmLHEGS-06231',
'EXO-RunIISummer15wmLHEGS-06232',
'EXO-RunIISummer15wmLHEGS-06233',
'EXO-RunIISummer15wmLHEGS-06234',
'EXO-RunIISummer15wmLHEGS-06235',
'EXO-RunIISummer15wmLHEGS-06236',
'EXO-RunIISummer15wmLHEGS-06237',
'EXO-RunIISummer15wmLHEGS-06238',
'EXO-RunIISummer15wmLHEGS-06239',
'EXO-RunIISummer15wmLHEGS-06240',
'EXO-RunIISummer15wmLHEGS-06241',
'EXO-RunIISummer15wmLHEGS-06242',
'EXO-RunIISummer15wmLHEGS-06243',
'EXO-RunIISummer15wmLHEGS-06244',
'EXO-RunIISummer15wmLHEGS-06245',
'EXO-RunIISummer15wmLHEGS-06246',
'EXO-RunIISummer15wmLHEGS-06247',
'EXO-RunIISummer15wmLHEGS-06248',
'EXO-RunIISummer15wmLHEGS-06249',
'EXO-RunIISummer15wmLHEGS-06250',
'EXO-RunIISummer15wmLHEGS-06251',
'EXO-RunIISummer15wmLHEGS-06252',
'EXO-RunIISummer15wmLHEGS-06253',
'EXO-RunIISummer15wmLHEGS-06254',
'EXO-RunIISummer15wmLHEGS-06255',
'EXO-RunIISummer15wmLHEGS-06256',
'EXO-RunIISummer15wmLHEGS-06257',
'EXO-RunIISummer15wmLHEGS-06258',
'EXO-RunIISummer15wmLHEGS-06259',
'EXO-RunIISummer15wmLHEGS-06260',
'EXO-RunIISummer15wmLHEGS-06261',
'EXO-RunIISummer15wmLHEGS-06262',
'EXO-RunIISummer15wmLHEGS-06263',
'EXO-RunIISummer15wmLHEGS-06264',
'EXO-RunIISummer15wmLHEGS-06265',
'EXO-RunIISummer15wmLHEGS-06266',
'EXO-RunIISummer15wmLHEGS-06267',
'EXO-RunIISummer15wmLHEGS-06268',
'EXO-RunIISummer15wmLHEGS-06269',
'EXO-RunIISummer15wmLHEGS-06270',
'EXO-RunIISummer15wmLHEGS-06271',
'EXO-RunIISummer15wmLHEGS-06272',
'EXO-RunIISummer15wmLHEGS-06273'
]

for request_prepid_to_clone in RequestsToClone:
    request = mcm.get('requests', request_prepid_to_clone)
    request[u'fragment'] = request[u'fragment'].replace('9000007','18').replace("\'18:all = dm dmbar 2 0 0 1 0.01 0.1 10 1\',\n",'').replace("\'18:isResonance = false\',\n",'')
    clone_answer = mcm.clone_request(request)
    if clone_answer.get('results'):
        print('Clone PrepID: %s' % (clone_answer['prepid']))
    else:
        print('Something went wrong while cloning a request. %s' % (dumps(clone_answer)))



