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

class IHersteller(form.Schema, IImageScaleTraversable):
    """
    Hersteller von Produkten oder Maschinen
    """

    anschrift1 = schema.TextLine(title = _(u"Anschrift 1"),
            description = _(u"Bitte geben Sie hier die Anschrift des Herstellers ein."),
            required = True,)

    anschrift2 = schema.TextLine(title = _(u"Anschrift 2"),
            description = _(u"Bitte geben Sie hier einen evtl. Adresszusatz des Herstellers ein."),
            required = False,)

    anschrift3 = schema.TextLine(title = _(u"Anschrift 3"),
            description = _(u"Bitte geben Sie hier einen evtl. weiteren Adresszusatz des Herstellers ein."),
            required = False,)

    land = schema.TextLine(title = _("Land"),
            description = _(u"Bitte geben Sie hier das Land des Herstellers ein."),
            required = True,)

    telefon = schema.TextLine(title = _("Telefonnummer"),
            description = _(u"Bitte geben Sie hier die vollständige Telefonnummer mit Ländercode ein,\
                              Beispiel: +49 (0) 30 12345/678"),
            required = True,)

    telefax = schema.TextLine(title = _("Faxnummer"),
            description = _(u"Bitte geben Sie hier die vollständige Telefaxnummer mit Ländercode ein,\
                              Beispiel: +49 (0) 30 12345/777"),
            required = False,)

    email = schema.TextLine(title = _("E-Mail Adresse"),
            description = _(u"Bitte geben Sie hier die E-Mailadresse des Herstellers ein."),
            required = False,)

    homepage = schema.URI(title = _("Hompage"),
            description = _(u"Bitte geben Sie hier die Internetadresse (http://www.example.de)\
                              des Herstellers ein."),
            required = False)

class Hersteller(Container):
    grok.implements(IHersteller)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# hersteller_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IHersteller)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
