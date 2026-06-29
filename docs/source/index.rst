***********************
apiFISH - Documentation
***********************

**Date**: |today| **Version**: |release|

.. add short description

====
User
====

.. panels::
    :card: + intro-card text-center
    :body: text-center p-2
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2

    ---
    .. image:: _static/getting_started/Download-Icon.png
       :height: 75

    +++

    .. link-button:: getting_started/installation
            :type: ref
            :text: Installation
            :classes: btn-block btn-info stretched-link text-white

    ---
    .. image:: _static/getting_started/jupyter_logo.png
       :height: 75

    +++

    .. link-button:: getting_started/tutorials
            :type: ref
            :text: Tutorials
            :classes: btn-block btn-info stretched-link text-white


=========
Developer
=========

.. panels::
    :card: + intro-card text-center
    :body: text-center p-2
    :footer: text-center p-2
    :column: col-lg-2 col-md-4 col-sm-6 col-xs-12 p-2
    
    ---
    .. image:: _static/home_page/developers.png
       :height: 50

    
    +++

    .. link-button:: development/contributing_to_apiFISH
            :type: ref
            :text: contributing to apiFISH
            :classes: stretched-link


    
    ---
    .. image:: _static/home_page/dev_install.jpg
       :height: 50

    
    +++

    .. link-button:: development/installation
            :type: ref
            :text: Developer installation
            :classes: stretched-link


    
    ---
    .. image:: _static/home_page/pep8.png
       :height: 50

    
    +++

    .. link-button:: development/coding_style
            :type: ref
            :text: coding style
            :classes: stretched-link


    
    ---
    .. image:: _static/home_page/process.svg
       :height: 50

    
    +++

    .. link-button:: development/process
            :type: ref
            :text: Development process
            :classes: stretched-link


    
    ---
    .. image:: _static/home_page/document.jpg
       :height: 50

    
    +++

    .. link-button:: development/document
            :type: ref
            :text: How to document
            :classes: stretched-link




.. toctree::
   :caption: Getting Started
   :hidden:

   getting_started/installation
   getting_started/tutorials

.. toctree::
   :caption: Reference
   :hidden:
   :maxdepth: 4

   
   reference/apidoc/apifish.filter
   reference/apidoc/apifish.formatting
   reference/apidoc/apifish.identification
   reference/apidoc/apifish.image
   reference/apidoc/apifish.matching
   reference/apidoc/apifish.registration
   reference/apidoc/apifish.visualization

.. toctree::
   :caption: Development
   :hidden:

   Contributing<development/contributing_to_apiFISH>
   Installation<development/installation>
   Convention<development/coding_style>
   development/process
   Documentation<development/document>

