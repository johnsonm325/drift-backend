PHONY_DATA = {'packages': [{'name': 'gcc',
                            'status': 'SAME',
                            'hosts': [{'host1.example.com': '8.2.1-6.fc29.x86_64'},
                                      {'host2.example.com': '8.2.1-6.fc29.x86_64'}]},
                           {'name': 'gcc-c++',
                            'status': 'SAME',
                            'hosts': [{'host1.example.com': '8.2.1-6.fc29.x86_64'},
                                      {'host2.example.com': '8.2.1-6.fc29.x86_64'}]},
                           {'name': 'gcc-gdb-plugin',
                            'status': 'SAME',
                            'hosts': [{'host1.example.com': '8.2.1-6.fc29.x86_64'},
                                      {'host2.example.com': '8.2.1-6.fc29.x86_64'}]},
                           {'name': 'robert_burns',
                            'status': 'UNKNOWN',
                            'hosts': [{'host1.example.com': '1.0-1.el99.noarch'},
                                      {'host2.example.com': None}]},
                           ],
              'facts': [{'name': 'uname.release',
                         'status': 'DIFF',
                         'hosts': [{'host1.example.com': '4.19.10-300.fc29.x86_64'},
                                   {'host2.example.com': '4.19.9-300.fc29.x86_64'}]},
                        {'name': 'lscpu.socket(s)',
                         'status': 'SAME',
                         'hosts': [{'host1.example.com': '1'}, {'host2.example.com': '1'}]}
                        ],
              'last_updated': [{'name': 'last_updated',
                                'status': None,
                                'hosts': [{'host1.example.com': '2019-01-25T19:14:09+00:00'},
                                          {'host2.example.com': '2019-01-25T15:12:55+00:00'}]}
                               ]}