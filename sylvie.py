#!/bin/python
import argparse
import math
import statistics
import sys
import codecs

SEPERATOR = ' '
NEWLINE = '\n'
INTERNAL_DATA = dict()
def parse_arguments():
    parser = argparse.ArgumentParser(description='Process data',
                                     prog='sylvie'
                                     )
    parser.add_argument('--file',
                        action='store',
                        required=False,
                        help='Which file to read from instead of stdin',
                        )
    parser.add_argument('--seperator',
                       action='store',
                       required=False,
                        help = 'Provide custom Seperator symbol',
                       )
    parser.add_argument('--color',
                        action='store_true',
                        required=False,
                        help='Whether to colorize output based on detected source code',
                        )
    parser.add_argument('--choice',
                        action='store',
                        required=False,
                        type=int,
                        help = 'Whether to provide interative choice between all options',
                        )
    parser.add_argument('--newline',
                        action='store',
                        required=False,
                        help='Provide custom newline symbol',
                        )
    parser.add_argument('--divert',
                        action='store',
                        required=False,
                        help='Divert output to some file or namedpipe ,while passing current output',
                        )
    parser.add_argument('--tabular',
                        action='store_true',
                        required=False,
                        help='Whether to start tabular parsing',
                        )
    parser.add_argument('--count',
                        action='store',
                        choices=['line','word'],
                        required=False,
                        help='Whether to count all input',
                        )
    parser.add_argument('--unique',
                        action='store',
                        choices=['line','word'],
                        required=False,
                        help='Whether to output only unique values'
                        )
    parser.add_argument('--sort',
                        action='store',
                        choices=['alpha','len','delen','ralpha'],
                        required=False,
                        help='How to sort the output',
                        )
    parser.add_argument('--linum',
                         action='store',
                         choices=['roman','arabic','word'],
                         required=False,
                         help='Whether to add line numbers to output'
                         )
    parser.add_argument('--output',
                         action='store',
                         required=False,
                         help='Output to file'
                         )
    parser.add_argument('--store',
                        action='store',
                        required=False,
                        help='Internal Variable to store current value'
                        )
    parser.add_argument('--var',
                        action='store',
                        required=False,
                        help='Internal Variable to load for further entanglement'
                        )
    parser.add_argument('--lower',
                        action='store_true',
                        required=False,
                        help='Whether to transform data to lowercase'
                        )
    parser.add_argument('--upper',
                        action='store_true',
                        required=False,
                        help='Whether to transform data to uppercase'
                        )
                        
    return parser.parse_args()

def setup_defaults(arguments):
    pass
    
def get_input(filename):
    data = None
    if filename:
        with open(filename) as inputfile:
            data = inputfile.read()
    else:
        data = codecs.decode(input(),'unicode_escape')
           
            
    return data
            
def choice_endpoint(data,default):
    global NEWLINE
    choices = data.split(NEWLINE)
    if default is None:
        print('Choices available')
        average_length = int(statistics.mean([ len(a) for a in choices ]))
        print('-'*average_length)
        for index , choice in enumerate(choices,1):
            print(' {index}. {choice} '.format(index=index,choice=choice))
        print('-'*average_length)
        index = int(input('Select index >>'))
    else:
        index = default
    return choices[index]
    

def divert_endpoint(data,filename):
    with open(filename,'w') as outputfile:
        outputfile.write(data)
    return data

def count_endpoint(data,strategy):
    global NEWLINE
    global SEPERATOR
    if strategy == 'word':
        return str(len(data.split(SEPERATOR)))
    elif strategy == 'line':
        return str(len(data.split(NEWLINE)))

def unique_endpoint(data,strategy):
    global SEPERATOR
    global NEWLINE
    if strategy == 'word':
        return SEPERATOR.join(set(data.split(SEPERATOR)))
    elif strategy == 'line':
        return NEWLINE.join(set(data.split(NEWLINE)))

def linum_endpoint(data,strategy):
    return data
    
def sort_endpoint(data,strategy):
    return data

def output_endpoint(data,filename):
    with open(filename,'w') as outputfile:
        outputfile.write(str(data))
    return None

def store_endpoint(data,varname):
    global INTERNAL_DATA
    INTERNAL_DATA[varname] = data
    return data
def var_endpoint(data,varname):
    global INTERNAL_DATA
    return INTERNAL_DATA.get(varname,'')
def tabular_endpoint(data,options):
    global NEWLINE
    table = data.split(NEWLINE)
    for i,option in enumerate(options):
        if option[:2] == '--':
            option = option[2:]
            if option == 'column':
                pass
def main():
    global INTERNAL_DATA
    arguments = parse_arguments()
    output = get_input(arguments.file)
    INTERNAL_DATA['input'] = output
    for argument_index , argument in enumerate(sys.argv[1:]):

        if argument[:2] == '--':
            argument = argument[2:]
            if argument == 'choice':
                output = choice_endpoint(output,arguments.choice)
            if argument == 'tabular':
                output = tabular_endpoint(output,sys.argv[argument_index+2:])
            if argument == 'divert':
                output = divert_endpoint(output,sys.argv[argument_index+2])
            if argument == 'count':
                output = count_endpoint(output,arguments.count)
            if argument == 'unique':
                output = unique_endpoint(output,arguments.unique)
            if argument == 'output':
                output = output_endpoint(output,arguments.output)
            if argument == 'store':
                output = store_endpoint(output,arguments.store)
            if argument == 'var':
                output = var_endpoint(output,arguments.var)
    if output:
        print(output)
        

main()
        
