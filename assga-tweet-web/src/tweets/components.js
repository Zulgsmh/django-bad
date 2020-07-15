import React, {useEffect, useState} from 'react'

import{loadTweets} from '../lookup'
//import {TweetsList} from '.'

export function TweetsComponents(props){
  const textAreaRef = React.createRef()
  const [newTweets, setNewTweets] = useState([])
  const handleSubmit = (event) => {
    event.preventDefault()
    const newVal = textAreaRef.current.value
    let tempNewTweets = [...newTweets]
    //server side call
    tempNewTweets.unshift({
      content: newVal,
      likes: 0,
      id: 1234,
    })
    setNewTweets(tempNewTweets)
    textAreaRef.current.value = ''
  }

  return <div className={props.className}>
          <div className='col-12'>
            <form onSubmit={handleSubmit}>
            <textarea ref={textAreaRef} className='form-control' required={true} placeholder="Tape ton tweet ici !">

            </textarea>
            <button type='submit' className='btn btn-primary my-3'> Tweet </button>
          </form>
          </div>
      <TweetsList newTweets={newTweets}/>
  </div>
}

//print my tweet list
export function TweetsList(props){
    const [tweetsInit, setTweetsInit] = useState([])
    const [tweets, setTweets] = useState([])
    //affiche le nouveau tweet + les anciens 
    useEffect(() => {
      const final = [...props.newTweets].concat(tweetsInit)
      if(final.length !== tweets.length){
        setTweets(final)
      }
    }, [props.newTweets, tweets, tweetsInit])

    useEffect( () => {
      const myCallback = (response, status) => {
        //console.log(response, status)
        if(status === 200){
          setTweetsInit(response)
        } else{
          alert("There was an error")
        }
      }
      loadTweets(myCallback)
    }, [tweetsInit])
    return tweets.map((item, index)=>{
      return <Tweet tweet={item} className= 'my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`}/>
    })
  }

//action btn
export function ActionBtn(props){
    const {tweet, action} = props
    const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0)
    const [userLike, setUserLike] = useState(tweet.userLike === true ? true : false)
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : 'Action'
    const handleClick = (event) => {
        event.preventDefault()
        if(action.type === 'like'){
          if(userLike === true){
            //unlike tweet
            setLikes(likes - 1)
            setUserLike(false)
          } else {
            //like tweet
            setLikes(likes + 1)
            setUserLike(true)
        }
    }
  }
  const display = action.type === 'like' ? `${likes} ${action.display}` : actionDisplay
  return <button className={className} onClick={handleClick}>{display}</button>
}


//print complete block of a tweet with action button
export function Tweet(props){
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
      <p>{tweet.id} - {tweet.content}</p>
        <div className='btn btn-group'>
          <ActionBtn  tweet={tweet} action={{type: "like", display: "Likes" }} />
          <ActionBtn  tweet={tweet} action={{type: "unlike", display: "Unlike" }} />
          <ActionBtn  tweet={tweet} action={{type: "retweet", display: "" }} />
        </div>
    </div>
  }