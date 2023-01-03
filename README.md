# Data Bot
Most users work with data on a day-to-day basis. 
Data interaction may range from organizing photos, organizing data in a company, or developing scientific workflows.
While different in complexity above use cases share functionalities like storing data, managing metadata or transforming data. 

There are solutions to tackle individual steps as well as the whole process.
Yet, we believe there is still room for improvement. 
For example, many solutions do not implement open standards, effectively locking users in their ecosystem. 
Other solutions process a small amount of data on a user's computer or a large amount of data on a cluster with nothing in between. 

As users, we should be able to define what data are and where they come from and transform them at will. 
It should be the responsibility of the software to keep track of the metadata and oversee the transformation process on local or remote machines. 
At the same time, the data, metadata, and transformation scripts must still be under the control of a user. 

In addition just producing metadata as another artefact bring no use.
As users we should be able to leverage metadata for tasks like search and data management.
Part, if not all, of this functionality is implemented in data catalogs. 
Metadata in data catalog can be represented using [DCAT] as an open standard to allow for easy integration.
On the other hand [data catalogs sometimes do not live up to their promise](https://www.dataengineeringweekly.com/p/data-catalog-a-broken-promise):
* Why is it so expensive in terms of the level of effort to roll out a data catalog solution?
* Despite the initial energy from the stakeholders, why does the usage of Data Catalogs keep declining?
While those questions mostly focus on an enterprise level, similar issues nerd to tackled for small groups or even personal use. 
The same article also propose a solution: 
* Lose the Interface and embedded into the data creation tools
* Expand from Data Catalog to Knowledge Engine - Aka not just a passive web portal, but integrate into the data creation process, aka Data Contract platform.
We plan to implement the proposals by generating DCAT compatible metadata automatically as user is manipulating the data.

## Resources
* Python Executing Commands : https://realpython.com/python-subprocess/
* Provenance Ontology : https://www.w3.org/TR/prov-primer/
* Linked Data Platform : https://www.w3.org/TR/ldp/
* Flask : https://flask.palletsprojects.com/en/2.1.x/
* DCAT : https://www.w3.org/TR/vocab-dcat-2/
* Python Concurrent IO : https://www.youtube.com/watch?v=GpqAQxH1Afc
