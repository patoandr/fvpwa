
if('serviceWorker' in navigator){
    console.log('Puedes usar serviceWorker')
    navigator.serviceWorker.register('./sw.js')
                           .then(res => console.log('serviceWorker cargado correctamente', res))
                           .catch(err => console.log('serviceWorker no se ha podido resgistrar', err))

}else{
    console.log('No se puede')
}