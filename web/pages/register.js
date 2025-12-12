import React from 'react';
import apiClient from '../utils/apiClient';

const Register = () => {
  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await apiClient.post('/auth/register', { email, password });
      // redirect to login page after successful register
    } catch (error) {
      // display error message
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <input type='text' value={email} onChange={(e) => setEmail(e.target.value)} placeholder='Email' />
      <input type='password' value={password} onChange={(e) => setPassword(e.target.value)} placeholder='Password' />
      <button type='submit'>Register</button>
    </form>
  );
};

export default Register;
