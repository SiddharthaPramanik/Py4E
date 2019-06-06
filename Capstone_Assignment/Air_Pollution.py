# Author : Siddhartha Pramanik

import urllib.request, urllib.parse
import json
import ssl
from matplotlib import pyplot as pt

# Method to print a json data in a proper format
def print_json_list(list):
    print(json.dumps(list, indent=4, sort_keys=True))


# Method to get the data from the API and write it to a file
def update_data(fname):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    fhandle = open(fname, "w+")
    serviceurl = (
        "https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?"
    )
    param = dict()
    param["api-key"] = "" # Place your api-key here
    param["format"] = "json"
    param["offset"] = "0"
    param["limit"] = "1000"
    param["filters"] = ""
    url = serviceurl + urllib.parse.urlencode(param)
    json_data = urllib.request.urlopen(url, context=ctx).read().decode()
    fhandle.write(json_data)
    fhandle.close()


# Method to create a list from the json data for a given state
def filter_data(fname, state_name):
    fhandle = open(fname)
    raw_data = fhandle.read()
    json_data = json.loads(raw_data)["records"]
    data_list = list()
    for item in json_data:
        if item["state"] != state_name:
            continue
        data_list.append(item)
    fhandle.close()
    return data_list


# Method to get the list of state from the saved json file
def state_list(fname):
    fhandle = open(fname)
    raw_data = fhandle.read()
    json_data = json.loads(raw_data)["records"]
    data_list = list()
    for item in json_data:
        if item["state"] not in data_list:
            data_list.append(item["state"])
    fhandle.close()
    return data_list


# Method to get the list of cities, given the name of state
def city_list(fname, state_name):
    filtered_list = filter_data(fname, state_name)
    data_list = list()
    for item in filtered_list:
        if item["city"] not in data_list:
            data_list.append(item["city"])
    return data_list


# Method to fill the missing data or 'NA' with 0
def clean_pollution_data(fname, state_name, pollutant_list):
    state_data = filter_data(fname, state_name)
    cities = city_list(fname, state_name)
    clean_pollutant_data = dict()
    for city in cities:
        pollutant_data = dict()
        for pollutant in pollutant_list:
            for data in state_data:
                if data["city"] != city:
                    continue
                if data["pollutant_id"] == pollutant:
                    if data["pollutant_avg"] == "NA":
                        pollutant_data[pollutant] = 0
                    else:
                        pollutant_data[pollutant] = int(data["pollutant_avg"])
        for pollutant in pollutant_list:
            if pollutant not in pollutant_data:
                pollutant_data[pollutant] = 0
        clean_pollutant_data[city] = pollutant_data
    return clean_pollutant_data, cities


# Method to get the data for a particular state from the clean data
def get_plot_data(clean_pollutant_data, cities, pollutant_list):
    plot_data_dict = dict()
    for pollutant in pollutant_list:
        plot_data_dict[pollutant] = []
    for city in cities:
        for pollutant in pollutant_list:
            plot_data_dict[pollutant].append(clean_pollutant_data[city][pollutant])
    for pollutant in pollutant_list:
        plot_data_dict[pollutant] = sum(plot_data_dict[pollutant]) / len(
            plot_data_dict[pollutant]
        )
    plot_data_list = [value for key, value in plot_data_dict.items()]
    return plot_data_list


# Method to plot the data using matplotlib
def plot_data(fname, pollutant_list):
    list_of_states = state_list(fname)
    for state in list_of_states:
        clean_pollutant_data, cities = clean_pollution_data(
            fname, state, pollutant_list
        )
        state_plot_data = get_plot_data(clean_pollutant_data, cities, pollutant_list)
        pt.scatter(pollutant_list, state_plot_data, label=state)
    pt.legend(loc="best")
    pt.title("Air Quality Inedx for India")
    pt.grid()
    pt.show()


# Program starts here
if __name__ == "__main__":
    fname = "air_pollution_data.json"
    pollutant_list = ["PM2.5", "PM10", "NO2", "NH3", "SO2", "CO", "OZONE"]
    update = input("Do you wish to fetch fresh data? [Y/N]")
    if update == "Y" or update == "y":
        update_data(fname)
    plot_data(fname, pollutant_list)

