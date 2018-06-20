'''
What’s in the ETL file?
1.	Definitions
    - Precise clarifications of any potentially ambiguous or unfamiliar terms used
2.	Data sources
    - list/table of fields and the database/table they come from
3.	Transformations
    - Operations
4.	Desired result:
    - For each analysis-ready table, list its dimensions and measures
5.	SQL
    - A working, fully reproducible SQL script that achieves #4

Example
=======

1.  Definitions

    Bulk penetration = percentage of revenue that came from units sold under a bulk discount
    Margin percent = Ratio of margin over price (not, e.g., price - cost)

2.  Data sources

    pr-edw-views-thd
        .SLS
        .POS_SLS_TRANS_DTL
    -------------------
    POS_TRANS_ID
    STR_NBR
    SKU_NBR
    SLS_DT
    UNT_SLS
    CURR_RTL_AMT

    analytics-pricing-team-thd
        .SHRD_VW_BL
        .BLK_PRCNG_DB2_XTRCT_HST_2018_02_21
    ---------------------
    SKU_NBR
    BLK_TIER1_QTY
    BLK_TIER1_DISC_AMT
    EFF_BGN_DT

3. Transformations

    - Modify price by the bulk discount percentage if units sold in a transaction meet the bulk quantity.
        - Pseudo-code:
            If UNT_SLS >= BLK_TIER1_QTY and SLS_DT >= EFF_BGN_DT:
                CURR_RTL_AMT = CURR_RTL_AMT*(100 - BLK_TIER1_DISC_AMT)/100

4. Result

    Transactions table
    Dimensions: SKU × store
    Measures: Total units sold, Total revenue, Bulk penetration

5. SQL

    Your beautiful SQL code here
'''
