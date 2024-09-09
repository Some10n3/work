import React, { section } from 'react'
import { useState } from 'react'
import { useEffect } from 'react'
import axios from 'axios'
import './App.css'
import LightSVG from './images/lightIcon.svg'
import DarkSVG from './images/darkIcon.svg'
import portrait from "./images/portrait.png"
import project1 from "./images/project_image_1.png"
import project2 from "./images/project_image_2.png"
import project3 from "./images/project_image_3.png"
import project4 from "./images/project_image_4.png"

const App = () => {

  const [courses, setCourses] = useState([])

  useEffect(() => {
      const fetchCourses = async () => {
          try {
              const res = await axios.get('http://localhost:8080/courses')
              setCourses(res.data)
              console.log(res)
          }
          catch (err) {
              console.log("err")
          }
      }
      fetchCourses()
  }, [])

  const groupCoursesBySemester = () => {
      const groupedCourses = {};
      courses.forEach(course => {
          if (!groupedCourses[course.semester]) {
              groupedCourses[course.semester] = [];
          }
          groupedCourses[course.semester].push(course);
      });
      return groupedCourses;
  };

  const groupedCourses = groupCoursesBySemester();

  const handleNavigateToContactMePage = () => {
    window.location.href = '/contact_me'
  }

  const openMiniNav = () => {
    document.getElementById('miniNav').classList.toggle('hidden')
  }

  const closeMiniNav = () => {
    document.getElementById('miniNav').classList.toggle('hidden')
  }

  const handleScroll = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  var darkModeBool = false

  const handleDarkMode = () => {
    darkModeBool = !darkModeBool
    if (darkModeBool === true) {
      document.getElementById('root').classList.add('dark')
      document.getElementById('root').classList.remove('light')
      document.getElementById('darkModeButton').classList.remove('md:block')
      document.getElementById('lightModeButton').classList.add('md:block')
    }
    else {
      document.getElementById('root').classList.add('light')
      document.getElementById('root').classList.remove('dark')
      document.getElementById('darkModeButton').classList.add('md:block')
      document.getElementById('lightModeButton').classList.remove('md:block')
    }
  }

  return(
    <section>
      <div className='mainDIV relative overflow-y-auto h-screen'>
        {/* Nav bar + Home */}
        <div className='relative z-10 h-1/2 md:h-screen bg-gradient-to-t from-DeepPurple-300 to-slate-200 dark:from-slate-900 '> {/*dark:to-slate-800 */}
          <nav className='fixed top-0 w-full bg-DeepPurple-200 p-5 z-10 dark:bg-slate-900'>
            <div className='w-full text-center'>
              <div className=' grid grid-cols-5 md:grid-cols-6 text-slate-800'>
                <a onClick={() => handleScroll('home')} className='hidden md:block nav'>Home</a>
                <a onClick={() => handleScroll('about')} className='hidden md:block nav'>About me</a>
                <a onClick={() => handleScroll('projects')} className='hidden md:block nav'>Projects</a>
                <a onClick={() => handleScroll('courses')} className='hidden md:block nav'>Courses taken</a>
                <a onClick={handleNavigateToContactMePage} className='hidden md:block nav'>Contact</a>
                <img src={DarkSVG} alt="Dark Icon" className='hidden md:block h-8 justify-self-center' onClick={handleDarkMode} id='darkModeButton'></img>
                <img src={LightSVG} alt="Light Icon" className='hidden h-8 justify-self-center' onClick={handleDarkMode} id='lightModeButton'></img>
              </div>
              <div className='md:hidden relative h-5'>
                <div onClick={openMiniNav} className='space-y-1 z-30 fixed'>
                  <div className='bg-DeepPurple-500 w-10 h-1 rounded-full dark:bg-slate-500'></div>
                  <div className='bg-DeepPurple-500 w-10 h-1 rounded-full dark:bg-slate-500'></div>
                  <div className='bg-DeepPurple-500 w-10 h-1 rounded-full dark:bg-slate-500'></div>
                </div>
                <div className='hidden' id='miniNav'>
                  <div className='bg-DeepPurple-300 h-1/2 w-screen rounded-b-xl fixed top-0 left-0 grid grid-rows-5 place-items-center z-20 dark:bg-slate-800'>
                    <a href='#home' className='nav' onClick={closeMiniNav}>Home</a>
                    <a href='#about' className='nav' onClick={closeMiniNav}>About me</a>
                    <a href='#projects' className='nav' onClick={closeMiniNav}>Projects</a>
                    <a href='#courses' className='nav' onClick={closeMiniNav}>Courses taken</a>
                    <a href='#contact' className='nav' onClick={closeMiniNav}>Contact</a>
                  </div>
                </div>
              </div>
            </div>
          </nav>
          <div id='home'>
            <div className=' container mx-auto py-32 px-24 md:py-96 dark:text-slate-400'>
              <div className='absolute bottom-0 text-xs md:bottom-20 md:text-base'>
                <h1 className='z-10'>Hi, my name is <span className='text-indigo-600'>Chanasorn</span></h1> <br />
                <h1 className='z-10'>I'm a Software Engineeering </h1> <br />
                <h1>student at KMITL university.</h1> <br />
              </div>
              <div className='z-0 absolute bottom-0 2xl:right-52 right-24 hidden xl:block'>
                <img src={portrait} alt='portrait.png' className=' max-w-sm z-0'></img>
              </div>
            </div>
          </div>
        </div>
        {/* About me */}
        <div id='about' className='darkBG'>
          <div className='container mx-auto py-16 text-center z-0'>
            <h1 className=' md:py-20 py-10 font-bold'>About me</h1>
            <div className='max-w-4xl mx-auto rounded-2xl bg-slate-300 p-12 hover:shadow-lg hover:overflow-hidden darkBG_children_container'>
              <h2 className='text-left logo-text'>My name is Chanasorn Howattanakulphong. </h2>
              <h2 className='text-left logo-text'>I'm a 3rd year Software Engineering student at KMITL.</h2>
              <h2 className='text-left logo-text'>I'm interested in <span className='text-indigo-600'>web development </span>and game development.</h2>
            </div>
            <h1 className=' md:py-20 py-10 font-bold text-indigo-600'>Web developing experience</h1>
            <div className='md:grid md:grid-cols-3 gap-y-4 min-h-fit'>
              <div className='col-span-3'>
                  <h1>Frontend</h1>
              </div>
              <div className="logo grid place-items-center">
                  <img src='https://cdnlogo.com/logos/h/84/html.svg' alt='HTMLLogo.svg' className='max-h-max_icon'></img>
              </div>
              <div className="logo grid place-items-center">
                  <img src='https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png' alt='JSLogo.png' className='max-h-max_icon'></img>
              </div>
              <div className="logo grid place-items-center">
                  <img src='https://www.seekpng.com/png/full/141-1415372_css3-icon-png.png' alt='cssLogo.svg' className='max-h-max_icon'></img>
              </div>
              <div className="text-center hidden md:block">
                  <h2 className='logo-text'>HTML</h2>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>JS</h2>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>CSS</h2>
              </div>
              <div className="logo grid place-items-center">
                  <img src='https://files.raycast.com/nwt9ncojkvwmjfkaada8upafvpnu' alt='TailwindLogo.svg' className='max-h-max_icon'></img>
              </div>
              <div className="logo grid place-items-center">
                <img src='https://cdn.worldvectorlogo.com/logos/react-2.svg' alt='ReactLogo.svg' className='max-h-max_icon'></img>
              </div>
              <div></div>
              <div className="text-center hidden md:block">
                  <h2 className='logo-text'>Tailwind</h2>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>React</h2>
              </div>
              <div></div>


              <div className='col-span-3  pt-16'>
                <h1>Backend</h1>
              </div>
              <div className="logo grid place-items-center">
                <img src='https://cdn.worldvectorlogo.com/logos/python-5.svg' alt='PythonLogo.svg' className='max-h-max_icon min-h-min_icon'></img>
              </div>
              <div className="logo grid place-items-center">
                <img src='https://ajeetchaulagain.com/static/7cb4af597964b0911fe71cb2f8148d64/87351/express-js.png' alt='ExpressJS.svg' className='max-h-max_icon min-h-min_icon'></img>
              </div>
              <div className="logo grid place-items-center">
                <img src='https://cdn.worldvectorlogo.com/logos/mysql-6.svg' alt='MySQLLogo.svg' className='max-h-max_icon min-h-min_icon'></img>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>Python</h2>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>ExpressJS</h2>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>MySQL</h2>
              </div>


              <div className='col-span-3 pt-16'>
                  <h1>API</h1>
              </div>
              <div className="logo grid place-items-center">
                  <img src='https://seeklogo.com/images/N/nodejs-logo-FBE122E377-seeklogo.com.png' alt='NodeJS.svg' className='max-h-max_icon min-h-min_icon'></img>
              </div>
              <div className="logo grid place-items-center">
                  <img src='https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png' alt='FastAPILogo.svg' className='max-h-max_icon min-h-min_icon'></img>
              </div>
              <div></div>
              <div className="text-center hidden md:block">
                  <h2 className='logo-text'>NodeJS</h2>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>FastAPI</h2>
              </div>
              <div></div>
              

            </div>

            <h1 className=' md:py-20 py-10 font-bold'>Other coding experiences</h1>
            <div className='md:grid md:grid-cols-3 gap-y-4 min-h-fit'>
              <div className="logo grid place-items-center">
                <img src='https://cdn.worldvectorlogo.com/logos/java.svg' alt='JavaLogo.svg' className='max-h-max_icon min-h-min_icon'></img>
              </div>
              <div className="logo grid place-items-center">
                <img src='https://cdn.worldvectorlogo.com/logos/lua-5.svg' alt='LuaLogo.svg' className='max-h-max_icon min-h-min_icon'></img>
              </div>
              <div className="logo grid place-items-center">
                <img src='https://cdn.worldvectorlogo.com/logos/c.svg' alt='CLogo.svg' className='max-h-max_icon min-h-min_icon'></img>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>Java</h2>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>Lua</h2>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>C++</h2>
              </div>
              <div className="logo grid place-items-center">
                <img src='https://cdn.worldvectorlogo.com/logos/rust.svg' alt='RustLogo.svg' className='max-h-max_icon min-h-min_icon'></img>
              </div>
              <div className="logo grid place-items-center">
                <img src='https://defold.com/images/logo/defold/logo/logo-ver-classic-white-160.png' alt='DefoldLogo.svg' className='max-h-max_icon min-h-min_icon'></img>  
              </div>
              <div></div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>Rust</h2>
              </div>
              <div className="text-center hidden md:block">
                <h2 className='logo-text'>Defold</h2>
              </div>
              <div></div>
            </div>
          </div>
        </div>
        {/* Projects */}
        <div className='bg-gradient-to-t from-DeepPurple-500 to-DeepPurple-300' id='projects'>
          <div className='container mx-auto py-16 text-center z-0 darkBG'>
              <h1 className=' md:py-20 py-10 font-bold'>Past projects</h1>
              <div className='grid grid-cols-1 gap-y-4 min-h-fit min-w-fit'>
                <div className='justify-self-center grid grid-cols-1 space-y-10 text-left'>
                  <h2 className='logo-text font-semibold'>Web programming semester project</h2>
                  <div className='mx-auto rounded-2xl max-w-xl'>
                    <img src={project1} alt='Project1.png' className='mx-auto rounded-2xl'></img>
                  </div>
                  <div className='max-w-4xl mx-auto rounded-2xl bg-slate-300 p-12 hover:shadow-lg hover:overflow-hidden darkBG_children_container'>
                    <h2 className='logo-text text-left font-semibold'>Explaination</h2>
                    <h2 className='logo-text text-left'>Me and my peers built a department website on JavaScript and FastAPI</h2>
                    <h2 className='logo-text text-left font-semibold'>Link to github</h2>
                    <a href='https://github.com/ksuperal/Web-Project' className='logo-text text-slate-800'>https://github.com/ksuperal/Web-Project</a>
                  </div>
                  <h2 className='logo-text font-semibold'>Object Oriented programming semester project</h2>
                  <div className='mx-auto rounded-2xl max-w-xs'>
                    <img src={project2} alt='Project2.png' className='mx-auto rounded-2xl'></img>
                  </div>
                  <div className='max-w-4xl mx-auto rounded-2xl bg-slate-300 p-12 hover:shadow-lg hover:overflow-hidden darkBG_children_container'>
                    <h2 className='logo-text text-left font-semibold'>Explaination</h2>
                    <h2 className='logo-text text-left'>My group made a bullet hell game using c++ with SFML library</h2>
                    <h2 className='logo-text text-left font-semibold'>Link to github</h2>
                    <a href='https://github.com/Some10n3/OOP_proj' className='logo-text text-slate-800'>https://github.com/Some10n3/OOP_proj</a>
                  </div>
                  <h2 className='logo-text font-semibold'>Pygame Project</h2>
                  <div className='mx-auto rounded-2xl max-w-xl'>
                    <img src={project3} alt='Project3.png' className='mx-auto rounded-2xl'></img>
                  </div>
                  <div className='max-w-4xl mx-auto rounded-2xl bg-slate-300 p-12 hover:shadow-lg hover:overflow-hidden darkBG_children_container'>
                    <h2 className='logo-text text-left font-semibold'>Explaination</h2>
                    <h2 className='logo-text text-left'>I made a rhythm game using pygame for my yr 1 semester project</h2>
                  </div>
                  <h2 className='logo-text font-semibold'>Lua bullet hell Project</h2>
                  <div className='mx-auto rounded-2xl max-w-xl'>
                    <img src={project4} alt='Project4.png' ></img>
                  </div>
                  <div className='max-w-4xl mx-auto rounded-2xl bg-slate-300 p-12 hover:shadow-lg hover:overflow-hidden darkBG_children_container'>
                    <h2 className='logo-text text-left font-semibold'>Explaination</h2>
                    <h2 className='logo-text text-left'>My highschool work utilizing lua with love2d engine.</h2>
                  </div>
                </div>
              </div>
          </div>
        </div>
        {/* Courses taken */}
        <div className='courses bg-DeepPurple-500 pb-10 darkBG' id='courses'>
          <div className='container mx-auto text-center space-y-3'>
            <h1 className='md:pt-36 md:pb-16 pt-12 pb-5 font-bold'>Courses I've taken</h1>
              {Object.keys(groupedCourses).map(semester => (
                  <div key={semester} className='max-w-4xl mx-auto rounded-2xl bg-slate-400 p-12 hover:shadow-lg hover:overflow-hidden text-center darkBG_children_container'>
                      <p className='text-4xl'>{`Semester ${semester}`}</p>
                      <div className='md:grid-cols-3'>
                          {groupedCourses[semester].map(course => (
                              <div key={course.id}>
                                  <p className='text-2xl'>{course.title}</p>
                              </div>
                          ))}
                      </div>
                  </div>
              ))}
          </div>
        </div>
        {/* Footer */}
        <div>
          <div className='w-full bg-DeepPurple-600 dark:bg-slate-950 dark:text-slate-300 p-5'>
            <div className='w-full text-center'>
              <div className='grid text-left'>
                <p className='text-md'>Email : Chanasorn.neo@gmail.com   Tel : 0864185772</p>
                <p className='text-md'>Github : https://github.com/Some10n3</p>
                <p className='text-md'>Linkedin : https://www.linkedin.com/in/chanasorn-howattanakulphong-4604712a2/</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
    </section>
  )
}

export default App