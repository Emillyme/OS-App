import React from 'react'

type Props = {}

function Login({}: Props) {
  
  return (
    <div className='flex flex-col w-[300px]'>
        <p>Login</p>
        <input type="text" className='border mb-2' placeholder='username' />
        <input type="text" className='border' placeholder='password'/>
        <button className='border bg-black text-white mt-5 cursor-pointer'>Login</button>
    </div>
  )
}

export default Login