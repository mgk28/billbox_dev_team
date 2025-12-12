import React from 'react';
import apiClient from '../utils/apiClient';

const Login = () => {
  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await apiClient.post('/auth/login', { email, password });
      localStorage.setItem('token', response.data.token);
      // redirect to homepage after successful login
    } catch (error) {
      // display error message
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input type='text' value={email} onChange={(e) => setEmail(e.target.value)} placeholder='Email' />
      <input type='password' value={password} onChange={(e) => setPassword(e.target.value)} placeholder='Password' />
      <button type='submit'>Login</button>
    </form>
  );
};

export default Login;
