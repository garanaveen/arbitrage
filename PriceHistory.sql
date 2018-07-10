BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS PriceHistory(
Exchange text,
TransactionType integer,
RelativeTimeStamp integer,
TimeStampStr text,
CurrencyCode text,
Price real
);

CREATE TABLE IF NOT EXISTS CurrentPrice(
Exchange text,
TransactionType integer,
CurrencyCode text,
Price real,
CONSTRAINT CurrentPrice_pk PRIMARY KEY (Exchange, TransactionType, CurrencyCode)
);

CREATE TABLE IF NOT EXISTS CurrentArbitrage(
Exchange1 text,
Exchange2 text,
TransactionType integer,
CurrencyCode text,
ArbitragePrice real,
CONSTRAINT CurrentPrice_pk PRIMARY KEY (Exchange1, Exchange2, TransactionType, CurrencyCode)
);

COMMIT;

