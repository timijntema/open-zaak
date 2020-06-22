.. _installation_cmis:

Using the CMIS adapter
======================

In order to use the CMIS adapter, the setting ``CMIS_ENABLED`` in the file ``src/openzaak/conf/includes/base.py`` should be set to ``True``:

    .. code-block:: python

        # File base.py

        CMIS_ENABLED = True

Then the following details need to be configured through the Admin interface of Open Zaak:

    1. The client URL
    2. The client username/password
    3. The name of the main folder in the Document Management System (DMS) where documents are going to be created

These can be configured under **Configuratie > CMIS configuration**. An example configuration could be:

    1. Client URL: ``http://example.com:8888/alfresco/api/-default-/public/cmis/versions/1.1/browser``
    2. Client Username: ``Admin``
    3. Client Password: ``SomeSecretPassw0rd``
    4. Main folder name: ``DRC``


The CMIS mapper
---------------

The file ``config/cmis_mapper.json`` is used to map the names of the properties of the objects that can be saved in the DMS from their Open Zaak names to the CMIS names.



Example CMIS request
--------------------

The example data below shows what data is sent by Open Zaak when a CMIS request is performed to create different objects.
The objects are created with a POST request to the url of the root folder. The url of the root folder is obtained by appending ``/root/`` to the client url configured in the Admin interface of Open Zaak.
For example, if the client url has been set to ``http://example.com/alfresco/api/-default-/public/cmis/versions/1.1/browser``, then the root folder url is ``http://example.com/alfresco/api/-default-/public/cmis/versions/1.1/browser/root``
The username and passwords used are those specified in the CMIS configuration section of the Admin interface.
The header of the POST request contains ``{"Accept": "application/json"}``.

**Document objects**

The data below is an example of what is sent from Open Zaak to create a document object.

    .. code-block::

        {
            'objectId': '5353495a-3441-42d5-bf52-f9388dc0eef8',
            'cmisaction': 'createDocument',
            'propertyId[0]': 'cmis:name',
            'propertyValue[0]': 'some titel-4IP28I',
            'propertyId[1]': 'cmis:objectTypeId',
            'propertyValue[1]': 'D:drc:document',
            'propertyId[2]': 'drc:document__identificatie',
            'propertyValue[2]': UUID('e6b0499e-c9ee-4473-b4fc-7f942564b2dc'),
            'propertyId[3]': 'drc:document__bronorganisatie',
            'propertyValue[3]': '768254103',
            'propertyId[4]': 'drc:document__creatiedatum',
            'propertyValue[4]': '2018-06-27T00:00:00.000Z',
            'propertyId[5]': 'drc:document__titel',
            'propertyValue[5]': 'some titel',
            'propertyId[6]': 'drc:document__auteur',
            'propertyValue[6]': 'some auteur',
            'propertyId[7]': 'drc:document__formaat',
            'propertyValue[7]': 'some formaat',
            'propertyId[8]': 'drc:document__taal',
            'propertyValue[8]': 'nld',
            'propertyId[9]': 'drc:document__informatieobjecttype',
            'propertyValue[9]': 'http://testserver/catalogi/api/v1/informatieobjecttypen/5b020631-8fd1-4f88-a237-b605f715e168',
            'propertyId[10]': 'drc:document__vertrouwelijkaanduiding',
            'propertyValue[10]': 'openbaar',
            'propertyId[11]': 'drc:document__beschrijving',
            'propertyValue[11]': 'old',
            'propertyId[12]': 'drc:document__begin_registratie',
            'propertyValue[12]': '2020-06-22T11:26:44.000Z',
        }


**Usage rights objects**

The data below is an example of what is sent from Open Zaak to create a usage right object.

    .. code-block::

        {
            'objectId': '0e921c3e-dbbb-47e7-bb57-81b5fc268daa',
            'cmisaction': 'createDocument',
            'propertyId[0]': 'cmis:name',
            'propertyValue[0]': 'TOX6GI',
            'propertyId[1]': 'cmis:objectTypeId',
            'propertyValue[1]': 'D:drc:gebruiksrechten',
            'propertyId[2]': 'drc:gebruiksrechten__startdatum',
            'propertyValue[2]': '2020-06-23T08:38:03.000Z',
            'propertyId[3]': 'drc:gebruiksrechten__omschrijving_voorwaarden',
            'propertyValue[3]': 'A sample description',
            'propertyId[4]': 'drc:gebruiksrechten__informatieobject',
            'propertyValue[4]': '/documenten/api/v1/enkelvoudiginformatieobjecten/5bd261cf-9fa0-4289-b5fc-a19f363b0f74'
        }
