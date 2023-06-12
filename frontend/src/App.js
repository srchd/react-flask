import React, { useState } from 'react'
import axios from 'axios'

function App() {
  const [members, setMembers] = useState([{}])

  function getMembers(){
   axios({
    method:'GET',
    url:'/members',
   }).then((res) => {
    const data = res.data
    setMembers(data)
   })
  }

  // function getData() {
  //   axios({
  //     method: "GET",
  //     url:"/profile",
  //   })
  //   .then((response) => {
  //     const res =response.data
  //     setMembers((res))
  //   }).catch((error) => {
  //     if (error.response) {
  //       console.log(error.response)
  //       console.log(error.response.status)
  //       console.log(error.response.headers)
  //       }
  //   })}

  return (
    <div>
      <button onClick={getMembers}>Get Members!</button>
      {(typeof members.members === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        members.members.map((mem, i) =>(
          <p key={i}>Member {i}: {mem}</p>
        ))
      )}
    </div>
  )
}

export default App