import React from 'react'

const LoadingStatus = ({theme}) => {
  return (
    <div className='loading-container'>
        <h1>Generating Your {theme} Story</h1>

        <div className='loading-animation'>
            <div className='loading-spinner'></div>
        </div>

        <p className='loading-info'>
          Please wait while we generate Your story ...
        </p>
    </div>
  )
}

export default LoadingStatus