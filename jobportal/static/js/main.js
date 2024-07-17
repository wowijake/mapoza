
document.addEventListener('DOMContentLoaded', () => {
    const filterJobForm = document.forms['filter_jobs']

    let filter = window.location.href

    if(!filter.includes('=')){
        filterJobForm['all'].checked = true
    }else{
        filter = filter.split('=')[1].toString()
        filterJobForm[filter].checked = true
    }

    filterJobForm.addEventListener('change', (event) => {
        if(event.target.name === 'filter' && event.target.checked){
            if(event.target.value === 'All' && event.target.checked){
                window.location.href = 'http://127.0.0.1:8000/jobs/'
            }else{
                const url = new URL('http://127.0.0.1:8000/jobs/')
                url.searchParams.append('filter', event.target.value)
                window.location.href = url.href
                console.log(url)
            }
        }
    })
})



