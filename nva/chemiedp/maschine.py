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

from nva.chemiedp.hersteller import IHersteller
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from nva.chemiedp import MessageFactory as _


# Interface class; used to define content-type schema.

class IMaschine(form.Schema, IImageScaleTraversable):
    """
    Druckmaschine oder Waschanlage
    """

    hersteller = RelationChoice(title = _(u"Hersteller"),
                 description = _(u"Bitte wählen Sie hier den Hersteller der Druckmaschine aus."),
                 source=ObjPathSourceBinder(object_provides=IHersteller.__identifier__),
                 required = True,)  

    bemerkungen = RichText(title=_(u"Bemerkungen"),
                  description=_(u"Hier können zusätliche Bemerkungen zur Maschine eingefügt werden."),
                  required=False,)

class Maschine(Container):
    grok.implements(IMaschine)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# maschine_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IMaschine)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
