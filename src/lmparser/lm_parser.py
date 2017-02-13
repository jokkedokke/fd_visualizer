# -*- coding: utf-8 -*-

import json
from pprint import pprint
import simplejson

with open('C:\\Users\\jouko\\PycharmProjects\\LongoMatchParser\\sample2.lgm','r') as json_data:
    d = simplejson.load(json_data)
    pallonhallinta={'Ajax':0,'OLS':0}

    for node in (y for y in d['Dashboard']['List'] if y['Name'] == 'PH Ajax'):
        for timer_event in node['Timer']['Nodes']:
            #print timer_event['Start']
            pallonhallinta['Ajax'] += timer_event['Stop'] - timer_event['Start']
        #pprint(node)
    print pallonhallinta['Ajax'] / 1000
    print pallonhallinta['Ajax'] / 1000 / 60.0

    for node in (y for y in d['Dashboard']['List'] if y['Name'] == 'PH OLS'):
        for timer_event in node['Timer']['Nodes']:
            pallonhallinta['OLS'] += timer_event['Stop'] - timer_event['Start']
    print pallonhallinta['OLS'] / 1000
    print pallonhallinta['OLS'] / 1000 / 60.0

    ols_syotto_ok = 0.0
    ols_syotto_nok = 0.0
    ajax_syotto_ok = 0.0
    ajax_syotto_nok = 0.0

    for node in (y for y in d['Timeline'] if u"Syöttö OLS" in y['Name']):
        for tag in node['Tags']:
            if tag['Value'] == 'Success':
                ols_syotto_ok = ols_syotto_ok + 1
            if tag['Value'] == 'Failure':
                ols_syotto_nok = ols_syotto_nok + 1

    for node in (y for y in d['Timeline'] if u"Syöttö Ajax" in y['Name']):
        for tag in node['Tags']:
            if tag['Value'] == 'Success':
                ajax_syotto_ok = ajax_syotto_ok + 1
            if tag['Value'] == 'Failure':
                ajax_syotto_nok = ajax_syotto_nok + 1

        # pprint(node)
    print "OLS OK: %d" % ols_syotto_ok
    print "OLS NOK: %d" % ols_syotto_nok
    print "OLS syöttöprosentti:  %f " % (ols_syotto_ok / ( ols_syotto_ok + ols_syotto_nok) * 100)
    print "Ajax OK: %d" % ajax_syotto_ok
    print "Ajax NOK: %d" % ajax_syotto_nok
    print "Ajax syöttöprosentti:  %f " % (ajax_syotto_ok / (ajax_syotto_ok + ajax_syotto_nok) * 100)