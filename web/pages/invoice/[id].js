import React from 'react';
import { useRouter } from 'next/router';
import apiClient from '../../utils/apiClient';

const Invoice = () => {
  const router = useRouter();
  const { id } = router.query;
  const [invoice, setInvoice] = React.useState(null);

  React.useEffect(() => {
    const fetchInvoice = async () => {
      try {
        const response = await apiClient.get(`/invoices/${id}`);
        setInvoice(response.data);
      } catch (error) {
        // handle error
      }
    };

    if (id) {
      fetchInvoice();
    }
  }, [id]);

  return (
    invoice && (
      <div>
        <h1>{invoice.title}</h1>
        <p>{invoice.description}</p>
        <p>{invoice.amount}</p>
      </div>
    )
  );
};

export default Invoice;
