
Quickstart
==========

This project is intended to be installed as a python package and cli tool. Note that it has been developed only for linux (although it should be somewhat simple to adapt to other operating systems). 

The tomtom API is used to retrieve free traffic data. An API key can be gotten by creating an account `here <https://developer.tomtom.com/>`_. 

Install the cli using ``pip install .``. 

The CLI has two subcommands, ``collect``, for making API calls to retrieve the data and ``inspect``, for handling data that has already been retrieved. Note that this CLI only works in instantaneous data, i.e. no historical data is accessed. Running ``zero-traffic-cli collect --collect-all`` will retrieve data for places listed in the config file. 

Use ``zero-traffic-cli inspect --generate-config`` to generate a configuration template. Here is a working example of the configuration file:

.. code-block:: 

    api_key: <your api key> 
    path_data_archive: <path to data folder of your choice> 
    id_latlon:
      - ['denver-I25@I76', 39.808889, -104.982778]
      - ['denver-I25@I70', 39.77019010470875, -104.99145451525855]
      - ['denver-I25@104th', 39.880795560153004, -104.9874785233745]
      - ['denver-I70@I76', 39.7840156288356, -105.09036747014535]
      - ['denver-I70W@Hwy40', 39.72740587149907, -105.17643151093101]

...note that you'll likely want to add your own places. The data archive path is a folder of your choosing (recommend to create an empty folder, subfolders and files will be automatically generated there). 

Each entry in ``id_latlon`` is a list with an arbitrary descriptor, a latitude and a longitude. These should be coordinates that are precisely located on the road where data collection is desirable. 


