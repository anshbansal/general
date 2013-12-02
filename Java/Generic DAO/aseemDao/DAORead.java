package aseemDao;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

import aseemEnums.TableName;

public interface DAORead {

	public abstract <T> List<T> getAll(Connection con, TableName tableName)
			throws SQLException;

	public abstract <T> List<T> getAllForInput(Connection con,
			TableName tableName, String columnName, String searchValue)
			throws SQLException;

	public abstract <T> T getPojoForPrimarKey(Connection con,
			TableName tableName, String primaryKey) throws SQLException;

	public abstract <T> boolean alreadyExisting(Connection con,
			TableName tableName, String primaryKey) throws SQLException;

	public abstract <T> boolean alreadyExisting(Connection con,
			TableName tableName, T currentPojo) throws SQLException;
}
