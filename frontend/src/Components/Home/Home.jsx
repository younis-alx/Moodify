import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './Home.css'

function Home(){
    const [inputValue, setInputValue] = useState('');
    const [error, setError] = useState('');
    const [hideError, setHideError] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        if (error) {
            setHideError(false);
            const timer = setTimeout(() => {
                setHideError(true);
            }, 2000);
            return () => clearTimeout(timer);
        }
    }, [error]);

    const handleInputChange = (event) => {
        setInputValue(event.target.value);
        setError(''); // Clear the error message when the input changes
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const url = new URL(inputValue);
            if (url.hostname !== 'twitter.com') {
                setError('Please enter a valid Twitter URL');
                return;
            }
        } catch (_) {
            setError('Please enter a valid URL');
            return;
        }
        const response = await fetch(process.env.FRONT_API, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: inputValue })
        });
        if (!response.ok) {
            setError('Failed to fetch data. Please try again.');
            return;
        }
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
            const data = await response.json();
            navigate('/dashboard', { state: { data: data } });
        } else {
            console.log(await response.json() + ' ' + contentType);
            setError('Received unexpected data from server.');
        }
    }

    return(
        <>
        <div className="home appear ">
            <img src='/logo.svg' alt="logo" className='logo'/>
            <form className="searchbar" onSubmit={handleSubmit}>
                <input type="text" placeholder="Twitter/X URL goes here..." onChange={handleInputChange} style={{borderColor: error ? 'red' : ''}}/>
                {error && <div className={`error-message ${hideError ? 'hide' : ''}`}>{error}</div>}
            </form>
        </div>
        </>
    );
}

export default Home;