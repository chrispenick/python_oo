import cmd, sys

class IFShell(cmd.Cmd):

    def precmd(self, line):
        return line.lower()

    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        print('going forward')
        
    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        print('going right')

    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        print('going left')

if __name__ == '__main__':
    IFShell().cmdloop()


    
