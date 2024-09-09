import React, { section } from 'react'
import { useState } from 'react'
import { useEffect } from 'react'
import axios from 'axios'
import './App.css'

const App = () => {

    const handleEmail = () => {
      const name = document.getElementById('name').value
      const email = document.getElementById('email').value
      const text = document.getElementById('message').value
      const data = {
        name : name,
        email : email,
        text : text
      }
      axios.post('http://localhost:8080/email', data)
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }

    return(
        <section className='h-full bg-gradient-to-t from-DeepPurple-300 to-white'>
            <div>
                <div className="container mx-auto">
                    <div className="flex flex-col gap-3 items-center pt-20">
                    <h1 className="text-indigo-600 font-bold">Contact me</h1>
                    </div>
                    <form className="mt-5 p-8 flex flex-col gap-5 items-center">
                    <input
                        className="p-2 w-full md:w-1/2 ring-1 ring-indigo-300 rounded-sm dark:bg-slate-800 dark:ring-0 dark:text-white"
                        type="text"
                        placeholder="Name Surname"
                        id='name'
                    />
                    <input
                        className="p-2 w-full md:w-1/2 ring-1 ring-indigo-300 rounded-sm dark:bg-slate-800 dark:ring-0 dark:text-white"
                        type="email"
                        placeholder="Email"
                        id='email'
                    />
                    <textarea
                        className="p-2 w-full md:w-1/2 ring-1 ring-indigo-300 rounded-sm dark:bg-slate-800 dark:ring-0 dark:text-white"
                        cols="30"
                        rows="10"
                        placeholder="Message..."
                        id='message'
                    ></textarea>
                    <button
                        className="w-1/2 bg-indigo-600 text-white font-medium px-3 py-2 rounded-md cursor-pointer"
                        onClick={handleEmail}
                    >
                        Submit
                    </button>
                    </form>
                </div>
            </div>
        </section>
    )
}

export default App