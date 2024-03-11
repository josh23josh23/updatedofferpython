import streamlit as st
import pandas as pd
import base64

# Assuming dfTransform and other necessary functions are defined

# Dictionary holding username:password pairs
users = {
    "grange": "grange2024",
}

# Function to check if the entered credentials are correct
def check_credentials(username, password):
    return username in users and users[username] == password

# Function for handling the authentication process
def login_page():
    st.title("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state['authenticated'] = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Function to set constants based on the region
def set_constants(region):
    global LotsPerNDH, AssumedNDA, SimplifiedStampDutyRate, AcquisitionCost, \
           SalesAndMarketingPercent, LegalFees, LandLoanInterestRate, \
           ConstructionLoanInterestRate, StatFees, ProjectManagementFeePercent, \
           ProjectContingencyPercent, LandHoldingFee, TargetProfitability, \
           GSTRate, TimePeriod, CPIAnnualRate, TPIAnnualRate, AnnualCapitalGrowth, \
           AnnualCapitalGrowthCompoundedRate, CPICompoundedRate, TPICompoundedRate

    LotsPerNDH = 14
    AssumedNDA = 1
    TimePeriod = 0

    if region == "WA":
        # Set WA constants
        LotsPerNDH = 14 #
        AssumedNDA = 1

        SimplifiedStampDutyRate = 0.051
        AcquisitionCost = 100000
        SalesAndMarketingPercent = 0.035
        LegalFees = 1000
        LandLoanInterestRate = .1
        ConstructionLoanInterestRate = 0.1
        StatFees = 50000
        ProjectManagementFeePercent = 0.035
        ProjectContingencyPercent = 0.05
        LandHoldingFee = 0.052
        TargetProfitability = 0.2
        GSTRate = 0.1
        TimePeriod = 0 
        CPIAnnualRate = 0.02
        TPIAnnualRate = 0.03
        AnnualCapitalGrowth = 0.07

    elif region == "QLD/NSW/SA":
        # Set QLD constants
        LotsPerNDH = 14 #
        AssumedNDA = 1
        
        SimplifiedStampDutyRate = 0.065
        AcquisitionCost = 100000
        SalesAndMarketingPercent = 0.035
        LegalFees = 1000
        LandLoanInterestRate = .1
        ConstructionLoanInterestRate = 0.1
        StatFees = 50000
        ProjectManagementFeePercent = 0.02
        ProjectContingencyPercent = 0.05
        LandHoldingFee = 0.052
        TargetProfitability = 0.2
        GSTRate = 0.1
        TimePeriod = 0 
        CPIAnnualRate = 0.02
        TPIAnnualRate = 0.03
        AnnualCapitalGrowth = 0.07

    # Calculate compounded rates
    AnnualCapitalGrowthCompoundedRate = (1 + AnnualCapitalGrowth)**TimePeriod
    CPICompoundedRate = (1 + CPIAnnualRate)**TimePeriod
    TPICompoundedRate = (1 + TPIAnnualRate)**TimePeriod
    

def generateDiscountProductType(RLV, NoofLots, zoning_category):
    WholeSaleValue = RLV #* NoofLots 
    #DiscountRequired = 0
    #ProductType = ""
    if zoning_category in ['Zoned', 'Residential Intensification']:
        if WholeSaleValue <= 5000:
            DiscountRequired = 0
            ProductType = "Super PPB"
            
        elif 5000 < WholeSaleValue <= 10000:
            DiscountRequired = 0
            ProductType = "Super PPB"

        elif 10000 < WholeSaleValue <= 20000:
            DiscountRequired = 0
            ProductType = "Super PPB"

        elif 20000 < WholeSaleValue <= 25000:
            DiscountRequired = 0
            ProductType = "Super PPB"

        elif 25000 < WholeSaleValue <= 30000:
            DiscountRequired = 0.25
            ProductType = "PPB"

        elif 30000 < WholeSaleValue <= 35000:
            DiscountRequired = 0.332
            ProductType = "PPB"
            
        elif 35000 < WholeSaleValue <= 40000:
            DiscountRequired = 0.435
            ProductType = "BMV"

        elif 40000 < WholeSaleValue <= 50000:
            DiscountRequired = 0.371
            ProductType = "BMV"
            
        elif 50000 < WholeSaleValue <= 60000:
            DiscountRequired = 0.33
            ProductType = "BMV"
        
        elif 60000 < WholeSaleValue <= 80000:
            DiscountRequired = 0.277
            ProductType = "BMV"
        
        elif 80000 < WholeSaleValue <= 100000:
            DiscountRequired = 0.246
            ProductType = "BMV"
        
        elif 100000 < WholeSaleValue <= 120000:
            DiscountRequired = 0.225
            ProductType = "BMV"

        elif 120000 < WholeSaleValue <= 140000:
            DiscountRequired = 0.209
            ProductType = "BMV"
            
        elif 140000 < WholeSaleValue <= 160000:
            DiscountRequired = 0.20
            ProductType = "BMV"
        
        else: 
            DiscountRequired = 0.2
            ProductType = "BMV"
    else:
        if WholeSaleValue <= 5000:
            DiscountRequired = 0
            ProductType = "Super PPB"
        
        elif 5000 < WholeSaleValue <= 10000:
            DiscountRequired = 0.1
            ProductType = "Super PPB"

        elif 10000 < WholeSaleValue <= 20000:
            DiscountRequired = 0.12
            ProductType = "Super PPB"

        elif 20000 < WholeSaleValue <= 25000:
            DiscountRequired = 0.17
            ProductType = "Super PPB"

        elif 25000 < WholeSaleValue <= 30000:
            DiscountRequired = 0.25
            ProductType = "PPB"

        elif 30000 < WholeSaleValue <= 35000:
            DiscountRequired = 0.332
            ProductType = "PPB"
            
        elif 35000 < WholeSaleValue <= 40000:
            DiscountRequired = 0.5
            ProductType = "BMV"

        elif 40000 < WholeSaleValue <= 50000:
            DiscountRequired = 0.5
            ProductType = "BMV"
            
        elif 50000 < WholeSaleValue <= 60000:
            DiscountRequired = 0.5
            ProductType = "BMV"
        
        elif 60000 < WholeSaleValue <= 80000:
            DiscountRequired = 0.5
            ProductType = "BMV"
        
        elif 80000 < WholeSaleValue <= 100000:
            DiscountRequired = 0.5
            ProductType = "BMV"
        
        elif 100000 < WholeSaleValue <= 120000:
            DiscountRequired = 0.5
            ProductType = "BMV"

        elif 120000 < WholeSaleValue <= 140000:
            DiscountRequired = 0.5
            ProductType = "BMV"
            
        elif 140000 < WholeSaleValue <= 160000:
            DiscountRequired = 0.5
            ProductType = "BMV"
        
        else: 
            DiscountRequired = 0.5
            ProductType = "BMV"
    
    return DiscountRequired, ProductType

def getDiscount(row):
    return row[0]  # Accessing the first element of the tuple

def getProduct(row):
    return row[1]  # Accessing the first element of the tuple

def dfTransform(dfSim):
    dfSim['Zoned / Rezone'] = dfSim['Zoned / Rezone']
    dfSim['Revenue per Lot'] = dfSim['Retail Lot Price'].astype("float")
    dfSim['OPC/ Construction Cost Per Lot'] = dfSim['OPC'].astype('float') 
    dfSim['Revenue per Lot Escalated'] = dfSim['Revenue per Lot']*AnnualCapitalGrowthCompoundedRate
    dfSim['NetRevenue(Less GST)'] = dfSim['Revenue per Lot Escalated']/(1+GSTRate)
    dfSim['OPC/ Construction Cost Per Lot Escalated'] = dfSim['OPC/ Construction Cost Per Lot']*TPICompoundedRate
    dfSim['No of Lots'] = dfSim['NDH']*(7000/dfSim['Min Lot Size'])
    dfSim['Acquisition Cost Per Lot'] = (AcquisitionCost*CPICompoundedRate)/dfSim['No of Lots']
    dfSim['Sales And Marketing'] = dfSim['Revenue per Lot Escalated']*SalesAndMarketingPercent + LegalFees
    dfSim['Interest and Finance without RLV'] = (AcquisitionCost*CPICompoundedRate)/dfSim['No of Lots']  + ConstructionLoanInterestRate*dfSim['OPC/ Construction Cost Per Lot Escalated']
    dfSim['Stat Fees per Lot'] = (StatFees*CPICompoundedRate)/dfSim['No of Lots'] 
    dfSim['Management Fees'] = dfSim['Revenue per Lot Escalated']*ProjectManagementFeePercent
    dfSim['Contingency'] = dfSim['OPC/ Construction Cost Per Lot Escalated']*ProjectContingencyPercent
    dfSim['Other Cost per Lot Without RLV'] = dfSim['Acquisition Cost Per Lot'] +dfSim['Sales And Marketing']+\
        dfSim['Interest and Finance without RLV'] + dfSim['Stat Fees per Lot'] + \
        dfSim['Management Fees'] + dfSim['Contingency']
    RSum = (SimplifiedStampDutyRate + LandLoanInterestRate + LandHoldingFee + 1)*(1+ TargetProfitability)
    dfSim['RLV'] = (dfSim['NetRevenue(Less GST)'] - dfSim['OPC/ Construction Cost Per Lot Escalated']*(1 + TargetProfitability)\
    -dfSim['Other Cost per Lot Without RLV']*(1 + TargetProfitability))/RSum
    dfSim['Stamp Duty'] = dfSim['RLV']*SimplifiedStampDutyRate
    dfSim['Interest and Finance RLV component'] = LandLoanInterestRate*dfSim['RLV']
    dfSim['Land Holding'] = LandHoldingFee*dfSim['RLV']
    dfSim['Other Cost per Lot with RLV Component'] = dfSim['Other Cost per Lot Without RLV'] + dfSim['Stamp Duty'] \
        + dfSim['Interest and Finance RLV component'] + dfSim['Land Holding']
    dfSim['Net Profit'] = dfSim['NetRevenue(Less GST)'] - dfSim['OPC/ Construction Cost Per Lot Escalated'] \
        - dfSim['Other Cost per Lot with RLV Component'] - dfSim['Land Holding'] - dfSim['RLV']
    dfSim['Total Development Cost'] = dfSim['OPC/ Construction Cost Per Lot Escalated'] + dfSim['Other Cost per Lot with RLV Component'] \
            +  dfSim['RLV']
    
    dfSim['TDC Check'] = dfSim['Net Profit'] / dfSim['Total Development Cost']
    dfSim['DiscountAndProductType'] = dfSim.apply(lambda row: generateDiscountProductType(row['RLV'], row['No of Lots'], row['Zoned / Rezone']), axis=1)
    dfSim['Discount'] = dfSim['DiscountAndProductType'].apply(getDiscount)
    dfSim['ProductType'] = dfSim['DiscountAndProductType'].apply(getProduct)
    dfSim.drop(columns=['DiscountAndProductType'], inplace=True)
    dfSim['OfferValuePercent']  = 1- dfSim['Discount']
    dfSim['Zone RLV'] = dfSim['RLV']*dfSim['No of Lots']
    dfSim['Zone Buy'] = dfSim['Zone RLV'] * dfSim['OfferValuePercent']
    return dfSim


def main_app():
    st.title("Select Your Region")
    choice = st.selectbox("Choose a region:", ["", "QLD/NSW/SA", "WA"])

    if choice:
        set_constants(choice)

        # Create a file uploader widget
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

        if uploaded_file is not None:
            # Read the uploaded file with Pandas
            df = pd.read_csv(uploaded_file)

            # Display the uploaded DataFrame
            st.write("Uploaded DataFrame:")
            st.write(df.head())

            if st.button('Process Figures'):
                st.markdown("### Processed Data")
                dfm = dfTransform(df)  # Ensure dfTransform is defined
                st.write(dfm.head())

                # Provide a download link for the modified DataFrame as CSV
                st.markdown("### Download Processed CSV File")
                modified_csv = dfm.to_csv(index=False)
                b64 = base64.b64encode(modified_csv.encode()).decode()
                href = f'<a href="data:file/csv;base64,{b64}" download="modified_file.csv">Click here to download</a>'
                st.markdown(href, unsafe_allow_html=True)


# Main function to orchestrate the app flow
def main():
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if st.session_state['authenticated']:
        main_app()
    else:
        login_page()

if __name__ == "__main__":
    main()
