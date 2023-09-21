import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
phone_number=input("enter phonenumber with country code")
#parsing string to number
pn=phonenumbers.parse(phone_number)

#printing the time zone
tz=timezone.time_zones_for_number(pn)

print("TimeZone:",str(tz))

#printing the location
location=geocoder.description_for_number(pn,'en')
print("Location:",str(location))


#printing the service provider
sp=carrier.name_for_number(pn,'en')
print("service provider:",str(sp))