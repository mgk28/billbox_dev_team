import React from 'react';
import apiClient from '../utils/apiClient';

const CreateInvoice = () => {
  const [title, setTitle] = React.useState('');
  const [description, setDescription] = React.useState('');
  const [amount, setAmount] = React.useState('');

  const handleCreate = async (e) => {
    e.preventDefault();
    try {
      await apiClient.post('/invoices', { title, description, amount });
      // redirect to invoices page after successful creation
    } catch (error) {
      // display error message
    }
  };

  return (
    <form onSubmit={handleCreate}>
      <input type='text' value={title} onChange={(e) => setTitle(e.target.value)} placeholder='Title' />
      <textarea value={description} onChange={(e) => setDescription(e.target.value)} placeholder='Description'></textarea>
      <input type='number' value={amount} onChange={(e) => setAmount(e.target.value)} placeholder='Amount' />
      <button type='submit'>Create</button>
    </form>
  );
};

export default CreateInvoice;
