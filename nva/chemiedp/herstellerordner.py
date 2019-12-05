# -*- coding: utf-8 -*-
from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from nva.chemiedp import MessageFactory as _


# Interface class; used to define content-type schema.

class IHerstellerOrdner(form.Schema, IImageScaleTraversable):
    """
    Ordner bzw. Tabelle Produkthersteller
    """
    titelbilder = RelationList(title=u"Titelbilder",
                           description=u"Hier können Sie Titelbilder für die Anzeige im Kopf der Seite auswählen",
                           default=[],
                           value_type=RelationChoice(title=_(u"Titelbilder"),
                                                     source=ObjPathSourceBinder()),
                           required=False,)

    anzeige = schema.Bool(title=u"Anzeige des Titelbildes im Ordner.",
                          default = True,
                          required = False,)

    spalte = schema.Bool(title=u"Anzeige des Titelbildes in der Zweispaltenansicht.",
                         default = True,
                         required = False,)

class HerstellerOrdner(Container):
    grok.implements(IHerstellerOrdner)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# herstellerordner_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IHerstellerOrdner)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
