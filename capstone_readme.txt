This capstone project for Python for informatics focuses on the pulling of data from the Seattle
open data crime data database.  The goal of the exersize is to create a proof of concept
on pulling in data, put it into a simple data model and then use a date range to populate a map using the google maps static api.

The current sets of code culminate in a url which returns the populated map.

Areas where the next iteration of code can improve on:

1. remove the use of a DB and pull the data directly from the Seattle Crime database.
Without a specific need to cache the data, there is no benefit saving to a db.

2. Update the Google maps API to use a different service.  The static maps api was good for
proof of concept but not for any level of scale in terms of the amount of data you desire
to visualize.

3. Create a sort by crime types.

4. update the visual markers for crime types.