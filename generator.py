from Open5GS import Open5GS
Open5GS_1 = Open5GS('127.0.0.1',27017)



slice_data = [
    {
      "sst": 1,
      "default_indicator": True,
      "session": [
        {
          "name": "internet",
          "type": 3, "pcc_rule": [], "ambr": {"uplink": {"value": 1, "unit": 3}, "downlink": {"value": 1, "unit": 3}},
          "qos": {
            "index": 9,
            "arp": {"priority_level": 8, "pre_emption_capability": 1, "pre_emption_vulnerability": 1}
          }
        }
      ]
    }
  ]

def sub_data(imsi):
    sub_data = {
            "imsi": imsi,
            "subscribed_rau_tau_timer": 12,
            "network_access_mode": 0,
            "subscriber_status": 0,
            "access_restriction_data": 32,
            "slice" : slice_data,
            "ambr": {"uplink": {"value": 1, "unit": 3}, "downlink": {"value": 1, "unit": 3}},
            "security": {
                "k": "465B5CE8 B199B49F AA5F0A2E E238A6BC",
                "amf": "8000",
                'op': None,
                "opc": "E8ED289D EBA952E4 283B54E8 8E6183CA"
                },
            "schema_version": 1,
            "__v": 0
            }
    return sub_data


if __name__ == "__main__":
    for subs in range (1000,2000):
        number = "51010000000{}".format(str(subs))
        subdata = sub_data(number)
        #print(Open5GS_1.DeleteSubscriber(number))
        #print(subdata)
        print(Open5GS_1.AddSubscriber(subdata))

#print(Open5GS_1.GetSubscribers()

