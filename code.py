# -*- encoding:utf-8 -*-
"""
  flaskext.actions.help_actions

"""
import os,sys
import utils


def show_urls(app):
    def action():
        """Displays all of the url matching routes for the project."""
        for rule in app.url_map.iter_rules():
            print "%-30s"%rule, rule.endpoint
    return action

def bshell(app):
    def action():
        """run shell use bpython
        """
        from bpython import embed
        embed({"app": app})
    return action

def compile_pyc(app,use_verbose=True):
    def action(directory=('d','.'),verbose=use_verbose):
        """Compile all python files in the directory into bytecode files.
        """
        import py_compile 
        for root, dirs, files in os.walk(directory):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext==".py":
                    full_path = os.path.abspath(os.path.join(root, file))
                    if verbose:
                        print "%sc" % full_path
                    py_compile.compile(full_path)

    return action

def clean(app,use_pretend=True,use_verbose=True):
    def action(directory=('d','.'),extention=('e','.pyc'),pretend=use_pretend,verbose=use_verbose):
        """
        Clean the specify filename extention files from the directory.
        :param pretend: Instead  of  actually performing the clean,just print it
        """
        check = lambda s: s.endswith(extention)
        if pretend:
            print "The following files are supposed to be delete:"
        else:
            print "the following files are removed:"
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filter(check, filenames):
                fullpath = os.path.abspath(os.path.join(dirpath, filename))
                if verbose:
                        print "%s" % fullpath
                if not pretend:
                    os.remove(fullpath)
    return action

def generate_secret_key(app):
    def action(length=('l',32)):
        """creates a new secret key"""
        print utils.generate_secret_key(length)
    return action

help_actionnames = {
        'bshell':bshell,
        'clean':clean,
        'compile_pyc':compile_pyc,
        'generate_secret_key':generate_secret_key,
        'show_urls':show_urls,
        }