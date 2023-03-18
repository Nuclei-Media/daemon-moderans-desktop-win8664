# migration to desktop

#### problem to solve

redis takes up too much client side resources. therefore the route of fetch needs to download the files and save them to a dedicated directory.

need to modify the syncing service to

## how to solve it

exchange the byte digestion routine for a local file cache. use encryption sharding to temporarily store the files. use a json file to store the file identity. files are stored as b64.

use a json file and migrate it upon initalisation for a application state.
