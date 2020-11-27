//Asignat nombre y version de la cache
const CACHE_NAME = 'v1_cache_FeriaVirtual';

//Ficheros a cachear en la aplicacion

var urlsToCache = [
    './',
];

//Evento install
//Instalacion del service Worker y guardar en cache los recursos estaticos
self.addEventListener('install', e => {
    e.waitUntil(
        caches.open(CACHE_NAME)
              .then(cache => {
                  return cache.addAll(urlsToCache)
                              .then(() => {
                                  self.skipWaiting();
                              })
              })
    )
});

//Evento activate

self.addEventListener('activate', e => {
    const cacheWhitelist = [CACHE_NAME];

    e.waitUntil(
        caches.keys()
              .then(cacheNames => {
                  return Promise.all(
                      cacheNames.map(cacheName => {

                        if(cacheWhitelist.indexOf(cacheName) === -1){
                            //Borrar elementos que no se necesitan
                            return caches.delete(cacheName);
                        }

                      })
                  )
              })
              .then(() => {
                  //Activar cache
                  self.clients.claim();
              })
    )
});

//Evento fetch
self.addEventListener('fetch', e => {

    e.respondWith(
        caches.match(e.request)
              .then(res => {
                  if(res){
                      //Devuelvo datos desde cache
                      return res;
                  }

                  return fetch(e.request);
              })
    )

});
