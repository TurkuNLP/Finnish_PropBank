import codecs
import collections
import sys

SenseData=collections.namedtuple("SenseData","base number description note description_fin note_fin link_original link_wordnet backtrack synset_id import_id")
ArgumentData=collections.namedtuple("ArgumentData","base number argnum definition note definition_fin note_fin")

def kill_null(s,default=u" "):
    if s==u"NULL":
        return default
    else:
        return s

def get_senses():
    bases={} #Key: base, value: "List of sensedata"
    args={} #Key: (base,sense) value: "List of argumentdata"
    with codecs.open("pb-defs.tsv","r","utf-8") as f:
        for lineno,line in enumerate(f):
            if lineno==0:
                continue
            s=SenseData(*(line.rstrip(u"\n").split(u"\t")))
            bases.setdefault(s.base,[]).append(s)
    with codecs.open("pb-argdefs.tsv","r","utf-8") as f:
        for lineno,line in enumerate(f):
            if lineno==0:
                continue
            tmp=line.strip().split(u"\t")
            a=ArgumentData(*(line.rstrip(u"\n").split(u"\t")))
            if not a.argnum.isdigit():
                print >> sys.stderr, line
                print >> sys.stderr, a.argnum
                continue
            args.setdefault((a.base,a.number),[]).append(a)
    for alist in args.itervalues():
        alist.sort(key=lambda a: int(a.argnum))
    return bases,args

def one_base(b,senses,args):
    senses=sorted(senses,key=lambda s:int(s.number))
    fname=u"../_lemmas/%s.md"%(b)
    with codecs.open(fname,"w","utf-8") as l:
        print >> l, u"---"
        print >> l, u"layout: lemma"
        print >> l, u"lemma:", b
        print >> l, u"---"
        print >> l
        for s in senses:
            print >> l, u"""<div class="sense">"""
            print >> l, u"#", u"""<span class="sensename">"""+b+u"."+s.number+u"""</span>"""
            print >> l
            print >> l, u"""<span class="description">"""+s.description+"""</span>"""
            print >> l
            if s.note != u"NULL":
                print >> l, s.note
                print >> l
            print >> l, u"""<span class="description">"""+s.description_fin+"""</span>"""
            print >> l
            if s.note_fin!=u"NULL":
                print >> l, s.note_fin
                print >> l
            if not (s.base,s.number) in args:
                print >> sys.stderr, "No args", (s.base,s.number)
            alist=args.get((s.base,s.number),[])
            if alist:
                for a in alist:
                    print >> l, u" | ".join((u"A"+a.argnum, a.definition, kill_null(a.note), a.definition_fin, kill_null(a.note_fin)))
                print >> l
            print >> l, u"""</div>"""
            print >> l
            


bases,args=get_senses()
for b,ss in sorted(bases.items()):
    one_base(b,ss,args)
