

//load tweets from db with django api 
export function loadTweets(callback){
    const xhr = new XMLHttpRequest()
    const method = 'GET' // 'POST'
    const url = "http://localhost:8000/tweets/api/all"
    const responseType = "json"   
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function(){
        callback(xhr.response, xhr.status)
        }
    xhr.onerror = function (e) {
      console.log(e)
      callback({"message": "The request was an error"}, 400)
    }
    xhr.send()
  } 