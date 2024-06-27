const boxs = [...document.querySelectorAll('.box')]
function updatedTime() {   
    boxs.forEach(x => { 
        // 日期   
        const country = new Date().toLocaleString("en-US", {
            timeZone: x.dataset.location
        })
        const timeZone = new Date(country)
        const month = new Date().toLocaleString("en-US", {
            timeZone: x.dataset.location,month: 'short'
        })
        x.querySelector(".date").innerText = `${timeZone.getDate()} ${month}.${timeZone.getFullYear()}`

        // 時間
        const hours = `0${timeZone.getHours()}`.slice(-2)
        const minutes = `0${timeZone.getMinutes()}`.slice(-2)
        x.querySelector(".time").innerText = `${hours}:${minutes}`
    })

}
updatedTime()
setInterval(updatedTime,1000)
