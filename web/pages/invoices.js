import React from 'react';
import apiClient from '../utils/apiClient';

const Invoices = () => {
  const [invoices, setInvoices] = React.useState([]);

  React.useEffect(() => {
    const fetchInvoices = async () => {
      try {
        const response = await apiClient.get('/invoices');
        setInvoices(response.data);
      } catch (error) {
        // handle error
      }
    };

    fetchInvoices();
  }, []);

  return (
    <div>
      <h1>Invoices</h1>
      {invoices.map((invoice) => (
        <div key={invoice.id}>{invoice.title}</div>
      ))}
    </div>
  );
};

export default Invoices;
