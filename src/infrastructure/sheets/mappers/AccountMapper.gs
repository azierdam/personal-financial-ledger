class AccountMapper {
  static toDomain(row) {
    if (!row[0] || !row[1]) throw new MalformedDataException('Invalid Account row');
    return new Account(row[0], row[1]);
  }
  static toRow(account) {
    return [account.accountId, account.name];
  }
}
