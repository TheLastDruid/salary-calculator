import React, { useState } from 'react';
import {
  Container,
  Paper,
  Typography,
  TextField,
  Button,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Grid,
  Box
} from '@mui/material';

function App() {
  const [formData, setFormData] = useState({
    position: '',
    period: ''
  });
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/api/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Typography variant="h4" gutterBottom align="center">
        Salary Calculator
      </Typography>
      
      <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={3}>
            <Grid item xs={12} md={6}>
              <FormControl fullWidth>
                <InputLabel>Position</InputLabel>
                <Select
                  name="position"
                  value={formData.position}
                  onChange={handleChange}
                  required
                >
                  <MenuItem value="OEP">OEP</MenuItem>
                  <MenuItem value="OE">OE</MenuItem>
                  <MenuItem value="CE">CE</MenuItem>
                </Select>
              </FormControl>
            </Grid>
            <Grid item xs={12} md={6}>
              <FormControl fullWidth>
                <InputLabel>Period</InputLabel>
                <Select
                  name="period"
                  value={formData.period}
                  onChange={handleChange}
                  required
                >
                  <MenuItem value="January">January</MenuItem>
                  <MenuItem value="July">July</MenuItem>
                </Select>
              </FormControl>
            </Grid>
            <Grid item xs={12}>
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
              >
                Calculate
              </Button>
            </Grid>
          </Grid>
        </form>
      </Paper>

      {result && (
        <Paper elevation={3} sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Results
          </Typography>
          <Grid container spacing={2}>
            <Grid item xs={12} md={6}>
              <Typography>Gross Salary: {result.salaire_brut} MAD</Typography>
              <Typography>Pension Deduction: {result.retenue_pension} MAD</Typography>
              <Typography>AMO Deduction: {result.retenue_amo} MAD</Typography>
              <Typography>Mutual Insurance: {result.retenue_mutuelle} MAD</Typography>
            </Grid>
            <Grid item xs={12} md={6}>
              <Typography>FOS: {result.fos} MAD</Typography>
              <Typography>Taxable Net: {result.salaire_net_imposable} MAD</Typography>
              <Typography>Income Tax: {result.impots} MAD</Typography>
              <Typography>Total Deductions: {result.total_retenus} MAD</Typography>
            </Grid>
            <Grid item xs={12}>
              <Box sx={{ mt: 2, p: 2, bgcolor: 'primary.light', borderRadius: 1 }}>
                <Typography variant="h6" color="white">
                  Net Salary: {result.salaire_net} MAD
                </Typography>
              </Box>
            </Grid>
          </Grid>
        </Paper>
      )}
    </Container>
  );
}

export default App;
