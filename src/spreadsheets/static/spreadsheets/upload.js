const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value 
const alertBox = document.getElementById('alert-box')

const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
            ${msg}
        </div>
    `
}

Dropzone.autoDiscover = false
const myDropzone = new Dropzone('#my-dropozne', {
    url: '/upload/',
    init: function() {
        this.on('sending', function(file, xhr, formData){
            console.log('sending')
            formData.append('csrfmiddlewaretoken', csrf)
        })
        this.on('success', function(file, response){
            console.log(response.ex)
            if(response.ex) {
                handleAlerts('perigo', 'Arquivo  já existe')
            } else {
                handleAlerts('sucesso', 'Seu arquivo foi baixado')
            }
        }) 
    },
    maxFiles: 1,
    maxFilesize: 3,
    acceptedFiles: '.xlsx'
})